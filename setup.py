from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='selenium_tools',

    version='0.1.0-alpha1',

    description='Selenium Tools to simplify interactions with complex elements',
    long_description=long_description,

    url='https://github.com/hcassus/selenium-tools-python',

    author='Henrique Cassus',
    author_email='henriquecasus@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    keywords='selenium webelement table tools',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['selenium'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)