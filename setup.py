# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in customization/__init__.py
from customization import __version__ as version

setup(
	name='customization',
	version=version,
	description='Customization',
	author='SILAP Company Limited',
	author_email='info@silap.net',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
