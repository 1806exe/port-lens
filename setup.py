"""setup.py: setuptools control file."""

import re
from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='port-lens',
    packages=['port_lens'],
    version='0.4',
    entry_points={
        "console_scripts": ["port-lens=port_lens.main:main"]
    },
    description='A simple port scanner that works.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/1806exe/port-lens',
    author='Inno Mgubhe',
    author_email='1806exe@email.com',
    license='MIT',
    zip_safe=False
)
