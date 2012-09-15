#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name                    =   'admin_bootstrap',
    version                 =   '0.7.0',
    description             =   'Django admin templates that are compatible with Twitter Bootstrap version 2.1.0',
    author                  =   'Daniel Ryan',
    author_email            =   'dryan@dryan.com',
    url                     =   'https://github.com/dryan/admin_bootstrap',
    packages                =   find_packages(),
    long_description        =   open('README', 'r').read(),
    license                 =   'BSD 3 Clause License',
    zip_safe                =   False,
    include_package_data    =   True,
)