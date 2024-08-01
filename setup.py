import setuptools
from setuptools import find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "CNN-Classifier"
AUTHOR_USER_NAME = "Manjunath-Bhashyam"
SRC_REPO = "CNN-Classifier"
AUTHOR_EMAIL = "manjunathbhashyam1995@gmail.com"

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
    packages=find_packages(where="src"),
    project_urls = {"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"}
)
