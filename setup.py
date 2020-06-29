# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in rapti_crm/__init__.py
from rapti_crm import __version__ as version

setup(
	name='rapti_crm',
	version=version,
	description='Customizations targetted for Rapti Gas Pvt Ltd by Atmark IT Solutions',
	author='Atmark IT Solutions',
	author_email='iamtribulation@outlook.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
