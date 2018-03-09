# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='LEDLights',
    version='0.1.0',
    description='LED Lights Tester',
    long_description=readme,
    author='Alan Treanor',
    author_email='alan.treanor@ucdconnect.ie',
    url='https://github.com/atreanor/LEDLights',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

