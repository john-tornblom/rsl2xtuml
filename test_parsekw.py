#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestParseKeywords(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_keyword_as_string(self, m):
        '.assign x = "${s:TEST}"'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = TMPL::parse_keyword(value: s, keyword: "TEST");')

    @rsl2xtuml.translate_docstring
    def test_keyword_as_variable(self, m):
        '.assign x = "${s:${kw}}"'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = TMPL::parse_keyword(value: s, keyword: kw);')


if __name__ == '__main__':
    unittest.main()

