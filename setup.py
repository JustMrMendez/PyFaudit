
from setuptools import setup, find_packages

setup(
    name='PyFaudit',
    version='0.1.0',
    packages=find_packages(),
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'PyFaudit = PyFaudit.scanner:main',
            'pyfaudit = PyFaudit.scanner:main',
        ],
    },
    # other metadata...
)

