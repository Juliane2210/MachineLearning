from setuptools import find_packages, setup
from typing import List


# defining a constant
HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return a list of requirements
    '''
    # Initialize an empty list named requirements
    requirements = []
    with open(file_path) as file_obj:
        # Reading lines from the file and storing them in the list
        requirements = file_obj.readlines()
        # Removing the newline characters
        [req.replace("\n", "")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='SupermarketSales',
    version='0.0.1',
    author='Juliane',
    author_email='bruck.juliane@gmail.com',
    # will consider any folder with an __init__.py file as a package
    packages=find_packages(),
    # when there are too many packages
    # ##it is best to create a fct using the requirements.txt file as an input
    install_requires=get_requirements('requirements.txt'),

)
