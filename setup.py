"""setup.py: setuptools control."""

import re
from setuptools import setup

setup(
    name='port-lens',
    packages=['port_lens'],
    version='0.1',
    entry_points={
        "console_scripts": ["port-lens=port_lens.main:main"]
    },
    description='A simple port scanner that works.',
    url='https://github.com/1806exe/port-lens',
    author='Inno Mgubhe',
    author_email='1806exe@email.com',
    license='MIT',
    zip_safe=False
)
