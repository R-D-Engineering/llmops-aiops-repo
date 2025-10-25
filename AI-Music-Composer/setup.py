from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI MUSIC COMPOSER",
    version="1.1.0",
    author="Anoop P Hegde",
    packages=find_packages(),
    install_requires = requirements,
)