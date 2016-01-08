#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestBinOp(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_plus(self, m):
        '.assign x = 1 + 1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (1 + 1);')
        
    @rsl2xtuml.translate_docstring
    def test_minus(self, m):
        '.assign x = 1 - 1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (1 - 1);')

    @rsl2xtuml.translate_docstring
    def test_unary_minus(self, m):
        '.assign x = 1 - -1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (1 - (- 1));')
        
    @rsl2xtuml.translate_docstring
    def test_mult(self, m):
        '.assign x = 2 * 2'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (2 * 2);')
        
    @rsl2xtuml.translate_docstring
    def test_div(self, m):
        '.assign x = 10 / 2'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (10 / 2);')
        
    @rsl2xtuml.translate_docstring
    def test_less(self, m):
        '.assign x = 0 < 1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (0 < 1);')
        
    @rsl2xtuml.translate_docstring
    def test_less_eq(self, m):
        '.assign x = 1 <= 1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (1 <= 1);')
        
    @rsl2xtuml.translate_docstring
    def test_not_eq(self, m):
        '.assign x = 1 != 1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (1 != 1);')
    
    @rsl2xtuml.translate_docstring
    def test_greater_eq(self, m):
        '.assign x = 1 >= 2'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (1 >= 2);')
        
    @rsl2xtuml.translate_docstring
    def test_eq(self, m):
        '.assign x = 0 == 1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (0 == 1);')
        
    @rsl2xtuml.translate_docstring
    def test_grouped_binop(self, m):
        '.assign x = (1 + 1)'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (1 + 1);')
        
    @rsl2xtuml.translate_docstring
    def test_chained_binop(self, m):
        '.assign x = (1 + 1) + 1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = ((1 + 1) + 1);')

    @rsl2xtuml.translate_docstring
    def test_chained_unaryop(self, m):
        '.assign x = not (1 == 1)'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (not (1 == 1));')

    @rsl2xtuml.translate_docstring
    def test_and(self, m):
        '.assign x = True and True'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (True and True);')
        
    @rsl2xtuml.translate_docstring
    def test_or(self, m):
        '.assign x = True or False'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (True or False);')
        
    @rsl2xtuml.translate_docstring
    def test_or_without_spaces(self, m):
        '.assign x = (True)or(False)'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = (True or False);')
        
    @rsl2xtuml.translate_docstring
    def test_pipe(self, m):
        '.assign a_set = a1_set | a2_set'
        self.fail('test case evaluation not implemented')
        
    @rsl2xtuml.translate_docstring
    def test_ampesand(self, m):
        '.assign a_set = a1_set & a2_set'
        self.fail('test case evaluation not implemented')
        
    @rsl2xtuml.translate_docstring
    def test_instance_plus_instance(self, m):
        self.fail('test case not implemented')
        
    @rsl2xtuml.translate_docstring
    def test_instance_minus_instance(self, m):
        self.fail('test case not implemented')
    

if __name__ == '__main__':
    unittest.main()

