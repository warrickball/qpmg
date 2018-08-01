from setuptools import setup

setup(
    name = 'qpmg',
    description = 'Quick Plotting for MESA or GYRE',
    version = '0.1',
    install_requires = ['numpy', 'matplotlib'],
    author = 'Warrick Ball',
    author_email = 'W.H.Ball@bham.ac.uk',
    url = 'https://github.com/warrickball/qpmg',
    scripts = ['qpmg'],
    license = 'MIT'
)
