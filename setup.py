from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="celebrity_detector_qa",
    version="0.1",
    packages=find_packages(),
    install_requires=requirements,
    author="Omprakash",
    author_email="omprakash070204@gmail.com",
    description="A Flask app for celebrity detection and Q&A using LLMs",
)