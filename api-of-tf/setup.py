#!/usr/bin/python
#-*- coding:utf-8 -*
###########################
#File Name: setup.py
#Author: gegey2008
#Mail: milkyang2008@126.com
#Created Time: 2017-11-01 22:44:22
############################

import sys
#导入包安装工具
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# explicitly config
test_args = [
    '--cov-report=term',
    '--cov-report=html',
    '--cov=tflearn',
    'tests'
]

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = test_args

    def run_tests(self ):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(name='tflearn',
      version='0.3.2',
      description='Deep learning Library featuring a higher-level API for TensorFlow',
      author='TfLearn contributors',
      author_email='aymeric.damien@gmail.com',
      url='https://github.com/tflearn/tflearn',
      download_url='https://github.com/tflearn/tflearn/tarball/0.3.2',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'numpy',
        'six',
        'pillow'
      ],
      test_suite='tests',
      cmdclass={'test': PyTest},
      classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
      ],
      keywords=[
        'TFLearn',
        'TensorFlow',
        'Deep Learning',
        'Machine Learning',
        'Neural Networks',
        'AI'
      ]
     )




