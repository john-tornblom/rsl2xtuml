#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestStringFormat(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_upperase(self, m):
        '.assign x = "$U{x}"'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = TMPL::transform(format: "U", text: x);')

    @rsl2xtuml.translate_docstring
    def test_upperase_and_underline(self, m):
        '.assign x = "$u_{x}"'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = TMPL::transform(format: "u_", text: x);')

    @rsl2xtuml.translate_docstring
    def test_dollar_dollar_in_literal(self, m):
        '.assign x = "$${baff}"'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = "$" + "{baff}";')

    @rsl2xtuml.translate_docstring
    def test_subst_in_subst(self, m):
        '''.//
        .assign a = "b"
        .assign b = "c"
        .assign x = "${${a}}"
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('a = "b";', lines.pop(0))
        self.assertEqual('b = "c";', lines.pop(0))
        self.assertEqual('x = "c";', lines.pop(0))


if __name__ == '__main__':
    unittest.main()

