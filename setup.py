from setuptools import setup

version = '0.1dev'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('TODO.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Django',
    'django-extensions',
    'django-nose',
    'lizard-ui >= 3.0',
    'pkginfo',
    ],

tests_require = [
    ]

setup(name='lizard-flot',
      version=version,
      description="Wrapper library for integration of Flot-based graphing in Lizard Map projects",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='Alexandr Seleznev',
      author_email='alexandr.seleznev@nelen-schuurmans.nl',
      url='https://github.com/lizardsystem/lizard-flot',
      license='GPL',
      packages=['lizard_flot'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require = {'test': tests_require},
      entry_points={
          'console_scripts': [
          ]},
      )
