from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dict-config-parser',
    version='1.0',
    description='A custom wrapper, written in python, for reading and writing ini files, using simple dictionaries.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thefakhir/dict_config_parser.git',
    author='M Fakhir Khan',
    author_email='thefakhir@gmail.com',
    keywords='config parser configparser',
    python_requires='>=3.5, <3.8',
    packages=['dict_config_parser']
)
