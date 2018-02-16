r"""
Plugin utils.
"""

def setupBuilder(builderModule, requirements=None, test_requirements=None):
  from setuptools import setup

  doc = getattr(builderModule, '__doc__') or ''
  moduleName = builderModule.__name__
  pluginName = builderModule.__plugin_name__

  setup(
    name='eka.plugins.builders.' + pluginName,
    url='',
    download_url='',
    license='MIT',
    version=getattr(builderModule, '__version__') or 'UNKNOWN',
    author=getattr(builderModule, '__author__') or 'UNKNOWN',
    author_email=getattr(builderModule, '__email__') or 'UNKNOWN',
    description=doc,
    long_description=doc,
    keywords= (getattr(builderModule, '__keywords__') or '') + ' builder eka plugin',
    platforms='any',
    packages=[moduleName],
    include_package_data=True,
    classifiers=[],
    install_requires=requirements or [],
    test_suite='tests',
    tests_require=test_requirements or [],
    zip_safe=False,

    entry_points={

      'eka.plugins.builders': [

         pluginName + '=' + moduleName,
      ]
    }
  )
