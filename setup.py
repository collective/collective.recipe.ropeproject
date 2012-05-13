from setuptools import setup, find_packages
import os

name = "collective.recipe.ropeproject"
version = '0.2'

read = lambda f: open(f).read()

long_description = (
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('README.rst')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' + 
    read('CHANGES.txt')
    # + '\n' +
    # 'Contributors\n' 
    # '************\n'
    # + '\n' +
    # read('CONTRIBUTORS.txt')
    )

setup(
    name = name,
    version = version,
    author = "Marcio Mazza",
    author_email = "marciomazza@gmail.com",
    description = "zc.buildout recipe for creating a .ropeproject with configured paths for eggs and dependencies",
    long_description = long_description,
    packages = find_packages('.'),
    include_package_data = True,
    package_dir = {'':'.'},
    namespace_packages = ['collective', 'collective.recipe'],
    install_requires = [
        'setuptools',
        'zc.recipe.egg',
        'rope'
    ],
    zip_safe=False,
    entry_points = {'zc.buildout': ['default = %s:Recipe' % name]},
    )
