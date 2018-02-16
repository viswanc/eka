r"""A compiler for Eka.
"""

from setuptools import setup, find_packages

# Data
requirements = []
test_requirements = []

import eka

setup(
  name='eka',
  version=eka.__version__,
  url='',
  download_url='',
  license='MIT',
  author=eka.__author__,
  author_email=eka.__email__,
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

  entry_points={
    'eka.plugins.classes': [

      'rest.server=p1:make_jpeg_image_plugin',
    ]
  }
)
