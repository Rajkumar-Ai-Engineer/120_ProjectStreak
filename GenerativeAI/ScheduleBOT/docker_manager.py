import docker
import os

def build_image(docker_client, image_name, context_path="."):
    """Builds a Docker image from a given path."""
    try:
        print(f"Building image '{image_name}' from context '{context_path}'.")
        image, build_logs = docker_client.images.build(path=context_path, tag=image_name)
        for chunk in build_logs:
            if 'stream' in chunk:
                print(chunk['stream'], end='')  # Print build output
        print(f"Successfully built image: {image.id}")
        return image
    except docker.errors.APIError as e:
        print(f"Error building image: {e}")
        return None

def create_and_run_container(docker_client, image, container_name="schedulebot_container", ports={'8000/tcp': 8000}, environment=None, volumes=None):
    """Creates and runs a Docker container from a given image."""
    try:
        print(f"Creating container '{container_name}' from image '{image.tags[0]}'.")
        container = docker_client.containers.run(
            image.tags[0],  # Use the image tag
            name=container_name,
            ports=ports,
            environment=environment,
            volumes=volumes,
            detach=True  # Run in detached mode
        )
        print(f"Container '{container.name}' started with ID: {container.id}")
        return container
    except docker.errors.APIError as e:
        print(f"Error creating container: {e}")
        return None

def stop_and_remove_container(docker_client, container):
    """Stops and removes a Docker container."""
    try:
        print(f"Stopping container '{container.name}'.")
        container.stop()
        print(f"Removing container '{container.name}'.")
        container.remove()
        print(f"Container '{container.name}' stopped and removed.")
    except docker.errors.APIError as e:
        print(f"Error stopping/removing container: {e}")

def main():
    """Main function to orchestrate Docker operations."""
    image_name = "schedulebot_image"
    container_name = "schedulebot_container"

    # Define the environment variables
    env_vars = {
        "PYTHONUNBUFFERED": 1,
        **dict(os.environ)  # Load existing environment variables
    }

    # Load .env file explicitly
    from dotenv import load_dotenv
    load_dotenv()

    # Include any environment variables defined in .env
    for key, value in os.environ.items():
        if key not in env_vars:
            env_vars[key] = value

    # Define the volumes
    volumes = {
        os.path.abspath('.'): {'bind': '/app', 'mode': 'rw'}
    }

    # Create a Docker client
    docker_client = docker.from_env()

    # Build the image
    image = build_image(docker_client, image_name)
    if not image:
        return

    # Create and run the container
    container = create_and_run_container(
        docker_client,
        image,
        container_name=container_name,
        ports={'8000/tcp': 8000},
        environment=env_vars,
        volumes=volumes
    )
    if not container:
        return

    try:
        # Keep the container running for some time (e.g., 60 seconds)
        print("Container is running.  Press Ctrl+C to stop and remove.")
        container.wait()  # Wait for the container to exit

    except KeyboardInterrupt:
        print("Stopping and removing container...")
    finally:
        # Stop and remove the container
        stop_and_remove_container(docker_client, container)

if __name__ == "__main__":
    main()