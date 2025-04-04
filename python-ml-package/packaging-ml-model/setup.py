import io
import os
from pathlib import Path
import chardet

from setuptools import find_packages, setup


# Metadata of package
NAME = 'prediction_model'
DESCRIPTION = 'Loan Prediction Model'
URL = 'https://github.com/sivanbhfe/AI_Doctorate_pythonpackaging'
EMAIL = 'sivan@gmail.com'
AUTHOR = 'Sivabalan'
REQUIRES_PYTHON = '>=3.7.0'

pwd = os.path.abspath(os.path.dirname(__file__))

# Get the list of packages to be installed

def detect_encoding(fname='requirements.txt'):
    with open(fname, 'rb') as f:
        raw_data = f.read()
        return chardet.detect(raw_data)['encoding']

def list_reqs(fname='requirements.txt'):
    encoding = detect_encoding(fname)
    with io.open(os.path.join(os.getcwd(), fname), encoding=encoding) as f:
        return f.read().splitlines()

try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}

with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'prediction_model': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)