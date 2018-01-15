"""A compiler for Eka."""

import os
import sys
from setuptools import setup, find_packages

# Data
requirements = []
test_requirements = []

import eka

setup(
	name='eka',
	version='0.0.1',
	url='',
	download_url='',
	license='MIT',
	author='',
	author_email='',
	description=__doc__,
	long_description=__doc__,
	zip_safe=False,
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
	],
	keywords='eka compiler',
	platforms='any',
	packages=find_packages(),
	include_package_data=True,
	install_requires=requirements,
	test_suite='tests',
	tests_require=test_requirements,
)
