from setuptools import setup, find_packages


# Import ``__version__`` variable
exec(open('{{ cookiecutter.package_name }}/_version.py').read())

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setuptools.setup(
    name="{{ cookiecutter.package_name }}",
    version=__version__,
    url="{{ cookiecutter.package_url }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.package_description }}",
    long_description=readme,
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[],
)
