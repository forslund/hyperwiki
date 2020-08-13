# -*- coding: utf-8 -*-
import codecs
import os
import re
import setuptools


def local_file(file):
  return codecs.open(
    os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8'
  )

install_reqs = [
  line.strip()
  for line in local_file('requirements.txt').readlines()
  if line.strip() != ''
]

version = re.search(
  "^__version__ = \((\d+), (\d+), (\d+)\)$",
  local_file('hyperwiki/__init__.py').read(),
  re.MULTILINE
).groups()


setuptools.setup(
  name = "hyperwiki",
  version = '.'.join(version),
  author = "Jonathan Goldsmith, Åke Forslund",
  author_email = "ake.forslund@gmail.com",
  description = "Wikipedia API over hyper for Python",
  license = "MIT",
  keywords = "python wikipedia API",
  url = "https://github.com/forslund/hyperwiki",
  install_requires = install_reqs,
  packages = ['hyperwiki'],
  long_description = local_file('README.rst').read(),
  classifiers = [
    'Development Status :: 4 - Beta',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3'
  ]
)
