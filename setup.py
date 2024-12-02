'''
The setup.py file is an essential part of packaging and distributing Python projects. 
It is used by setuptools (or distutils in older Python versions) to define the configuration of your project. such as its metadata, dependencies, and more.
It contains metadata and instructions for building and installing the project. 

- from setuptools import setup`: This line imports the setup function from the setuptools library, which is used to define the project's configuration.
- setup()`: This is the main function that defines the project's configuration. It takes a dictionary of arguments that specify various aspects of the project.
- name`: The name of the project.
- version`: The version number of the project.
- author`: The author of the project.
- author_email`: The email address of the project's author.
- description`: A short description of the project.
- long_description`: A longer description of the project.
- long_description_content_type`: The type of content in the long description (e.g., text or markdown).
- url`: The URL of the project's homepage.
- packages`: A list of packages that should be included in the distribution.
- install_requires`: A list of dependencies that should be installed when the project is installed.
- classifiers`: A list of classifiers that help categorize the project.
- python_requires`: The version of Python that the project requires.
- entry_points`: A dictionary of entry points that define how the project should be used.

'''


from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return the list of the requiremnts

    '''
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                ## Ignore the empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst



setup(
    name = "NetworkSecurity",
    version = "0.0.0.1",
    author = "Suraj Mishra",
    author_email = "msuraj20@.yahoo.com",
    packages= find_packages(),
    install_requires = get_requirements()
)
