# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 2023

@author: ywkgrrk1765
"""
from setuptools import setup
from setuptools import find_packages

def requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
      name='lungsound_analysis',
      version='0.0.0',
      description='this is a summary of the functional groups used in lung sound analysis',
      author='ywkgrrk1765',
      url='https://github.com/ywkgrrk1765/lungsound_analysis',
      packages=find_packages(),
      python_requires='>=3.7',
      install_requires=requires_from_file('requirements.txt'),
)
