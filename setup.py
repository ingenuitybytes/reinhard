#!/usr/bin/env python3
'''This is the setup.py file for the REINHARD Discord bot.
It is used to install the bot as a package.
'''

# Import modules and files
from setuptools import setup, find_packages


setup(
    name='reinhard',
    version='0.1.0',
    description='A Discord bot created with discord.py',
    author='Alois Zimmermann',
    author_email='alois.zimmermann2003@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ]
)