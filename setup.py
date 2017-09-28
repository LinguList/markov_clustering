import os
from setuptools import setup
import sys

if sys.version_info[0] < 3:
    raise Exception('markov_clustering requires Python 3')

distmeta = {}
for line in open(os.path.join('markov_clustering', '__init__.py')):
    try:
        field, value = (x.strip() for x in line.split('='))
    except ValueError:
        continue
    if field == '__version_info__':
        value = value.strip('[]()')
        value = '.'.join(x.strip(' \'"') for x in value.split(','))
    else:
        value = value.strip('\'"')
    distmeta[field] = value
    
try:
    with open("README.md") as readme:
        long_description = readme.read()
except IOError:
    long_description = "See {}".format(distmeta["__homepage__"])

setup(
    name="markov_clustering",
    version=distmeta["__version_info__"],
    description="Implementation of the Markov clustering (MCL) algorithm in python.",
    long_description=long_description,
    author=distmeta["__author__"],
    author_email=distmeta["__contact__"],
    url=distmeta["__homepage__"],
    license="MIT",
    platforms=["linux"],
    packages=["markov_clustering"],
    install_requires=[
        "numpy",
        "scipy",
        "scikit-learn"
    ],
    entry_points={
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Linux",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "License :: MIT License",
    ],
    keywords = "bioinformatics clustering"
)
