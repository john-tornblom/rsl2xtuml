#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestParseKeywords(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_keyword_as_string(self, rc):
        '.assign x = "${s:TEST}"'
        self.assertEqual('x = TMPL::parse_keyword(value: s, keyword: "TEST");', rc)

    @rsl2xtuml.translate_docstring
    def test_keyword_as_variable(self, rc):
        '.assign x = "${s:${kw}}"'
        self.assertEqual('x = TMPL::parse_keyword(value: s, keyword: kw);', rc)


if __name__ == '__main__':
    unittest.main()

