# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('LICENSE') as f:
    license = f.read()

with open('README.md') as f:
    readme = f.read()

setup(
    name='GoCrawl',
    version='0.1.0',
    description='GoCardless\' crawler',
    long_description=readme,
    author='Stephane Bruckert',
    author_email='contact@stephanebruckert.com',
    url='https://github.com/stephanebruckert/GoCrawl',
    license=license,
    packages=find_packages(exclude=('tests'))
)
