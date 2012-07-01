from setuptools import setup, find_packages
import os

name = "collective.recipe.ropeproject"
version = '0.2'

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

setup(
    name = name,
    version = version,
    author = "Marcio Mazza",
    author_email = "marciomazza@gmail.com",
    description = "zc.buildout recipe that creates a rope project config with python_path pointing to some eggs and their dependencies",
    long_description = long_description,
    packages = find_packages(exclude=['ez_setup']),
    include_package_data = True,
    package_dir = {'':'.'},
    namespace_packages = ['collective', 'collective.recipe'],
    install_requires = ['setuptools', 'zc.buildout', 'zc.recipe.egg', 'rope',],
    tests_require = ['zope.testing', 'zc.buildout>=1.5.2', 'zc.recipe.egg',],
    test_suite = 'collective.recipe.ropeproject.tests.test_docs.test_suite',
    zip_safe=False,
    entry_points = {'zc.buildout': ['default = %s:Recipe' % name]},
    )
