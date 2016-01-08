#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestEmit(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_emit(self, m):
        '''Hello world
        .emit to file "testfile"
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('TMPL::append(text: "Hello world" + "\\n");', lines.pop(0))
        self.assertEqual('TMPL::emit(filename: "testfile");',          lines.pop(0))
    
    @rsl2xtuml.translate_docstring    
    def test_emit_without_linebreak_case1(self, m):
        '''Hello\
        world'''
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'TMPL::append(text: "Hello        world" + "\\n");')
        

if __name__ == '__main__':
    unittest.main()

