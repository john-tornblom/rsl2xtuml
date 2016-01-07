#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestIfStatements(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def testPrintString(self, s):
        '.print "Hello world"'
        self.assertEqual('LOG::LogInfo(message: "Hello world");', s)


if __name__ == '__main__':
    unittest.main()

