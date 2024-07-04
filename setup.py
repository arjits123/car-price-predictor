from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This funciton will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',' ') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

# Considered as a metadata information of the project
setup(
    name='Car-price-predictor',
    version='0.0.1',
    author='Arjit',
    author_email='arjitpkt96@gmail.com',
    packages=find_packages(), # finds where the __init__.py file in all folders
    install_requires = get_requirements('requirements.txt')
)