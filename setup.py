from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    hyphen_dot_e = "-e ."
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if hyphen_dot_e in requirements:
            requirements.remove(hyphen_dot_e)
    return requirements


setup(
    name="mlproject",
    version="0.1",
    author="Kshitij",
    author_email="kshitij@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
