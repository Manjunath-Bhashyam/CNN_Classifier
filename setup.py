import setuptools
from typing import List

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "CNN-Classifier"
AUTHOR_USER_NAME = "Manjunath-Bhashyam"
SRC_REPO = "deepclassifier"
AUTHOR_EMAIL = "manjunathbhashyam1995@gmail.com"
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """
    Description: This function is used to return requirements list mention in requirements.txt file
    returns: This function is going to return a list which contains the names of libraries
    mentioned in requirements.txt file
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    description="Python Package for CNN app",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    project_urls = {"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
    install_requires=get_requirements_list()
)
