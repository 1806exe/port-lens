"""setup.py: setuptools control."""


import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('port-lens/main.py').read(),
    re.M
    ).group(1)

setup(name='port-lens',
version=version,
entry_points = {
        "console_scripts": ['port-lens = port-lens.port-lens:main']
        },
description='A simple port scanner that works.',
url='https://github.com/1806exe/port-lens',
author='Inno Mgubhe',
author_email='1806exe@email.com',
license='MIT',
packages=['port-lens'],
zip_safe=False)
