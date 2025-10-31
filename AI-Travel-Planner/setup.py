from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI TRAVEL AGENT",
    version="1.2",
    author="Anoop P Hegde",
    packages=find_packages(),
    install_requires = requirements,
)