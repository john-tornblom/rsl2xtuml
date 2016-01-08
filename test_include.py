#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestInclude(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_absolute_include(self, m):
        '.include "/tmp/rsl2xtuml.test.inc"'
        self.fail('test case evaluation not yet implemented')

    @rsl2xtuml.translate_docstring
    def test_relative_include(self, m):
        '.include "rsl2xtuml.test.inc"'
        self.fail('test case evaluation not yet implemented')


if __name__ == '__main__':
    unittest.main()

