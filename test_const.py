#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestConstLiterals(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_positive_integer(self, m):
        '.assign x = 1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = 1;')

    @rsl2xtuml.translate_docstring
    def test_negative_integer(self, m):
        '.assign x = -1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (- 1);')

    @rsl2xtuml.translate_docstring
    def test_positive_real(self, m):
        '.assign x = 1.1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = 1.1;')
        
    @rsl2xtuml.translate_docstring
    def test_negative_real(self, m):
        '.assign x = -1.1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (- 1.1);')

    @rsl2xtuml.translate_docstring
    def test_true(self, m):
        '.assign x = true'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = true;')
        
    @rsl2xtuml.translate_docstring
    def test_false(self, m):
        '.assign x = false'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = false;')
        
    @rsl2xtuml.translate_docstring
    def test_string(self, m):
        '.assign x = "Hello"'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = "Hello";')

    @rsl2xtuml.translate_docstring
    def test_empty_string(self, m):
        '.assign x = ""'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = "";')
        

if __name__ == '__main__':
    unittest.main()

