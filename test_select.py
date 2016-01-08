#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestSelect(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_select_any(self, m):
        '.select any a from instances of A'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'select any a from instances of A;')

    @rsl2xtuml.translate_docstring        
    def test_select_many(self, m):
        '.select many a_set from instances of A'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'select many a_set from instances of A;')
        
    @rsl2xtuml.translate_docstring
    def test_navigate_one(self, m):
        '.select one b related by a->B[R1]'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'select one b related by a->B[R1];')

    @rsl2xtuml.translate_docstring
    def test_navigate_any(self, m):
        '.select any b related by a->B[R1]'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'select any b related by a->B[R1];')

    @rsl2xtuml.translate_docstring
    def test_navigate_many(self, m):
        '.select many b_set related by a->B[R1]'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'select many b_set related by a->B[R1];')

    @rsl2xtuml.translate_docstring
    def test_navigate_one_reflexive(self, m):
        ".select one second_inst related by first_inst->A[R1.'next']"
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         "select one second_inst related by first_inst->A[R1.'next'];")
        
    @rsl2xtuml.translate_docstring
    def test_navigate_any_substitution(self, m):
        '.select any a from instances of A where ("${selected->B[R1].name}" == "Test")'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'select any a from instances of A where ("${selected->B[R1].name}" == "Test")')
        
    @rsl2xtuml.translate_docstring
    def test_select_with_many_spaces(self, m):
        '.select       any        a       from          instances       of      A'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'select any a from instances of A;')

    @rsl2xtuml.translate_docstring
    def test_select_with_type_names(self, m):
        '.select any string from instances of A'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'select any string from instances of A;')
        

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    unittest.main()

