#    This is a list of files to install Geatpy
#
#    Geatpy is a free toolbox: you can redistribute it and/or modify
#    it as you want.
#
#    Geatpy is distributed in the hope that it will be useful for the genetic 
#    and evolutionary algorithm, you can get the tutorial from http://www.geatpy.com
#
#    If you want to donate to it, please e-mail jazzbin@geatpy.com

from setuptools import setup, find_packages
import codecs
import os

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname), encoding='UTF-8').read()

LONG_DESCRIPTION = read("README.rst")

setup(name = "geatpy",
    version = "1.0.0",
    description = "This is Geatpy for Python",
    author = "Geatpy Team",
    author_email = "jazzbin@geatpy.com",
    url = "http://www.geatpy.com",
    packages= find_packages(),
    Scripts = ["geatpy/*"],
    include_package_data = True,    # Enabled list file: MANIFEST.in
    install_requires=[
        'numpy>=1.10.0',
        'matplotlib>=1.5.1',
    ],
    classifiers = [
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    ],
    long_description = LONG_DESCRIPTION,
    zip_safe = False,
)
