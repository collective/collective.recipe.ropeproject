from setuptools import setup, find_packages

name = "il.recipe.ropeproject"
version = '1.0b1'

# TODO: remove defaults
setup(
    name = name,
    version = version,
    author = "Marcio Mazza",
    author_email = "marciomazza@gmail.com",
    description = "Buildout recipe for creating a .ropeproject with configured paths of eggs and dependencies",
    packages = find_packages('.'),
    include_package_data = True,
    package_dir = {'':'.'},
    namespace_packages = ['il', 'il.recipe'],
    install_requires = [
        'zc.recipe.egg',
        'rope'
    ],
    zip_safe=False,
    entry_points = {'zc.buildout': ['default = %s:Recipe' % name]},
    )
