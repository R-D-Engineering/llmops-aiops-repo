from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Study Buddy AI",
    version="1.1",
    author="Anoop P Hegde",
    packages=find_packages(),
    install_requires = requirements,
)