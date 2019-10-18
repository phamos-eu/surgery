# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in surgery/__init__.py
from surgery import __version__ as version

setup(
	name='surgery',
	version=version,
	description='Surgery',
	author='tüit GmbH',
	author_email='info@tueit.de',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
