# -*- coding: utf-8 -*-

import doctest
import unittest
import shutil

import pkg_resources
from zc.buildout.testing import buildoutSetUp
from zc.buildout.testing import buildoutTearDown
from zc.buildout.testing import install
from zc.buildout.testing import install_develop

import os

test_dir = os.path.abspath(os.path.dirname(__file__))

def setUp(test):
    buildoutSetUp(test)
    install_develop('zc.recipe.egg', test)
    install_develop('collective.recipe.ropeproject', test)

def tearDown(test):
    buildoutTearDown(test)
    sample_buildout = test.globs['sample_buildout']
    shutil.rmtree(sample_buildout, ignore_errors=True)

def test_suite():
    suite = []
    flags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE |
        doctest.REPORT_NDIFF)

    suite.append(doctest.DocFileSuite('ropeproject.txt', globs=globals(),
                                      setUp=setUp, tearDown=tearDown,
                                      optionflags=flags,
                                      ))

    return unittest.TestSuite(suite)
