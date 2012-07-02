from setuptools import setup, find_packages
import os

name = "collective.recipe.ropeproject"
version = '1.0b3dev'

read = lambda f: open(f).read()

long_description = """
========================
 Detailed Documentation
========================
%s
%s

================
 Change history
================
%s

==============
 Contributors
==============
%s
""" % (read('README.rst'),
       read('collective/recipe/ropeproject/tests/ropeproject.txt'),
       read('CHANGES.txt'),
       read('CONTRIBUTORS.txt'),)

install_requires=['setuptools', 'zc.buildout', 'zc.recipe.egg', 'rope'],
tests_require=['zope.testing', 'zc.buildout>=1.5.2', 'zc.recipe.egg'],

setup(
    name=name,
    version=version,
    description="zc.buildout recipe that creates a rope project config with python_path pointing to some eggs and their dependencies",
    long_description=long_description,
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
    keywords='buildout eggs rope refactoring emacs vim',
    author="Marcio Mazza",
    author_email="marciomazza@gmail.com",
    url='https://github.com/collective/collective.recipe.ropeproject',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.recipe'],
    include_package_data=True,
    zip_safe=False,
    package_dir={'':'.'},
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
    test_suite='collective.recipe.ropeproject.tests.test_docs.test_suite',
    entry_points={'zc.buildout': ['default = %s:Recipe' % name]},
    )
