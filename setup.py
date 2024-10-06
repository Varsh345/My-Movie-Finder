from setuptools import setup, find_packages

with open("README.md","r",encoding = "utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'DHANA VARSHINI'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = 'movie_recommendation_system',
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'varshu2256@gmail.com',
    description = 'A small example package for movies recommendation',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = find_packages(where = SRC_REPO),
    package_dir = {'': SRC_REPO},
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
)