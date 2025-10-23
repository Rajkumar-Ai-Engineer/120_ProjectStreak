from setuptools import setup

setup(
    name="ContextArchitect",
    version="0.1.0",
    description="Context Architecture",
    author="Rajkumar",
    author_email="tech84602@gmail.com",
    py_modules=["helper"],
    install_requires=[
        "langchain==0.1.0",
        "llama-index==0.9.46",
    ],
)