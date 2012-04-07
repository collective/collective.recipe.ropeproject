from setuptools import setup, find_packages

name = "mz.recipe.ropemacs"
version = '0.1dev'

# TODO: rever se nao estou repetindo defaults
setup(
    name = name,
    version = version,
    author = "Marcio Mazza",
    author_email = "marciomazza@gmail.com",
    description = "Buildout recipe for creating a .ropemacs file with configured path for dependencies",
    packages = find_packages('.'),
    include_package_data = True,
    package_dir = {'':'.'},
    namespace_packages = ['mz', 'mz.recipe'],
    install_requires = [
        'zc.recipe.egg',
        'rope'
    ],
    zip_safe=False,
    entry_points = {'zc.buildout': ['default = %s:Recipe' % name]},
    )
