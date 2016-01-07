#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestConstLiterals(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def testPositiveInteger(self, rc):
        '.assign x = 1'
        self.assertEqual('x = 1;', rc)

    @rsl2xtuml.translate_docstring
    def testNegativeInteger(self, rc):
        '.assign x = -1'
        self.assertEqual('x = (- 1);', rc)

    @rsl2xtuml.translate_docstring
    def testPositiveReal(self, rc):
        '.assign x = 1.1'
        self.assertEqual('x = 1.1;', rc)
        
    @rsl2xtuml.translate_docstring
    def testNegativeReal(self, rc):
        '.assign x = -1.1'
        self.assertEqual('x = (- 1.1);', rc)

    @rsl2xtuml.translate_docstring
    def testTrue(self, rc):
        '.assign x = true'
        self.assertEqual('x = true;', rc)
        
    @rsl2xtuml.translate_docstring
    def testFalse(self, rc):
        '.assign x = false'
        self.assertEqual('x = false;', rc)
        
    @rsl2xtuml.translate_docstring
    def testString(self, rc):
        '.assign x = "Hello"'
        self.assertEqual('x = "Hello";', rc)

    @rsl2xtuml.translate_docstring
    def testEmptyString(self, rc):
        '.assign x = ""'
        self.assertEqual('x = "";', rc)
        

if __name__ == '__main__':
    unittest.main()

