import os 

paths = ["./requirements.txt", "./pyproject.toml", "./.env", "./src/__init__.py","./src/main.py","./src/app.py","./src/templates/index.html","./src/static/style.css","./src/helper.py"]


for path in paths:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        open(path, 'w').close()
print("All files and directories created successfully.")