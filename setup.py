
from setuptools import setup, find_packages

setup(
    name='PyFaudit',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'PyFaudit = PyFaudit.scanner:main',
            'pyfaudit = PyFaudit.scanner:main',
        ],
    },
    # other metadata...
)

