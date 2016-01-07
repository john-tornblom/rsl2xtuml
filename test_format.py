#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestConstLiterals(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def testUpperCase(self, rc):
        '.assign x = "$U{x}"'
        self.assertEqual('x = TMPL::transform(format: "U", text: x);', rc)

    @rsl2xtuml.translate_docstring
    def testExampleC_(self, rc):
        '.assign x = "$c_{x}"'
        self.assertEqual('x = TMPL::transform(format: "c_", text: x);', rc)

    @rsl2xtuml.translate_docstring
    def testDollarDollarInLiteral(self,rc):
        '.assign x = "$${baff}"'
        self.assertEqual('x = "$" + "{baff}";', rc)

    @rsl2xtuml.translate_docstring
    def testSubstInSubst(self, rc):
        '''.//
        .assign a = "b"
        .assign b = "c"
        .assign x = "${${a}}"
        '''
        lines = rc.splitlines()
        self.assertEqual('a = "b";', lines.pop(0))
        self.assertEqual('b = "c";', lines.pop(0))
        self.assertEqual('x = "c";', lines.pop(0))


if __name__ == '__main__':
    unittest.main()

