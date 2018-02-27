r"""
Plugin utils.
"""

def setup(pluginModule, requirements=None, test_requirements=None):
  from setuptools import setup

  doc = getattr(pluginModule, '__doc__') or ''
  moduleName = pluginModule.__name__
  pluginName = pluginModule.__plugin_name__

  setup(
    name='eka.plugins.classes.' + pluginName,
    url='',
    download_url='',
    license='MIT',
    version=getattr(pluginModule, '__version__') or 'UNKNOWN',
    author=getattr(pluginModule, '__author__') or 'UNKNOWN',
    author_email=getattr(pluginModule, '__email__') or 'UNKNOWN',
    description=doc,
    long_description=doc,
    keywords=(getattr(pluginModule, '__keywords__') or '') + ' builder eka plugin',
    platforms='any',
    packages=[moduleName],
    include_package_data=True,
    classifiers=[],
    install_requires=requirements or [],
    test_suite='tests',
    tests_require=test_requirements or [],
    zip_safe=False,
    entry_points={

      'eka.plugins.classes': [

         pluginName + '=' + moduleName,
      ]
    }
  )
