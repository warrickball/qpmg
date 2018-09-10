from setuptools import setup

setup(
    name = 'qpmg',
    description = 'Quick Plotting for MESA or GYRE',
    long_description=open('README.rst').read(),
    version = '0.2.2',
    install_requires = ['numpy', 'matplotlib'],
    author = 'Warrick Ball',
    author_email = 'W.H.Ball@bham.ac.uk',
    url = 'https://github.com/warrickball/qpmg',
    scripts = ['qpmg'],
    license = 'MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
        ]
)
