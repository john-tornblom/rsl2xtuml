#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestIfStatements(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_if(self, m):
        '''.//
        .if (true)
               .assign x = 0
           .end if
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('if true',   lines.pop(0))
        self.assertEqual('    x = 0;', lines.pop(0))
        self.assertEqual('else',       lines.pop(0))
        self.assertEqual('end if;',    lines.pop(0))

    @rsl2xtuml.translate_docstring
    def test_if_else(self, m):
        '''.//
        .if (false)
            .assign x = 0
        .else
            .assign x = 1
        .end if
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('if false',   lines.pop(0))
        self.assertEqual('    x = 0;', lines.pop(0))
        self.assertEqual('else',       lines.pop(0))
        self.assertEqual('    x = 1;', lines.pop(0))
        self.assertEqual('end if;',    lines.pop(0))
        
    @rsl2xtuml.translate_docstring
    def test_if_elif(self, m):
        '''.//
        .if (false)
            .assign x = 0
        .elif (true)
            .assign x = 1
        .end if'''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('if false',   lines.pop(0))
        self.assertEqual('    x = 0;', lines.pop(0))
        self.assertEqual('elif true',  lines.pop(0))
        self.assertEqual('    x = 1;', lines.pop(0))
        self.assertEqual('else',       lines.pop(0))
        self.assertEqual('end if;',    lines.pop(0))

    @rsl2xtuml.translate_docstring
    def test_if_elif_else(self, m):
        '''.//
        .if (false)
            .assign x = 0
        .elif (false)
            .assign x = 1
        .else
            .assign x = 2
        .end if'''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('if false',   lines.pop(0))
        self.assertEqual('    x = 0;', lines.pop(0))
        self.assertEqual('elif false', lines.pop(0))
        self.assertEqual('    x = 1;', lines.pop(0))
        self.assertEqual('else',       lines.pop(0))
        self.assertEqual('    x = 2;', lines.pop(0))
        self.assertEqual('end if;',    lines.pop(0))
        
        
        
if __name__ == '__main__':
    unittest.main()

