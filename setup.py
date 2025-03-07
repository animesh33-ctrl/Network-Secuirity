from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    """
    This function will return list of requirements
    """
    req_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                req = line.strip()
                # ignore empty lines and -e.
                if req and req != '-e .':
                    req_lst.append(req)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return req_lst

print(get_requirements())


setup(
    name='NetworkSecuirity',
    version='0.0.1',
    author='Animesh',
    author_email='paluianimesh31@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)