from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="RAG Medical Chatbot",
    version="1.0.0",
    author="Anoop P Hegde",
    packages=find_packages(),
    install_requires = requirements,
)