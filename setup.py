from setuptools import find_packages, setup
from typing import List


def get_requirements()->List[str]:

    requirements=List[str]=[]
    return requirements


setup(
    name="Heart disease",
    versiom="0.0.1",
    author="shreshth",
    author_email="goswamishreshth100@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements(),
)