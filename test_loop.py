#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestLoop(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_while_loop(self, m):
        '''.//
        .while (x > 0)
            .assign x = x - 1
        .end while
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('while (x > 0)',    lines.pop(0))
        self.assertEqual('    x = (x - 1);', lines.pop(0))
        self.assertEqual('end while;',       lines.pop(0))
        
    @rsl2xtuml.translate_docstring
    def test_while_loop_with_break(self, m):
        '''.//
        .while (x > 0)
            .if (x == 5)
                .break while
            .end if
            .assign x = x - 1
        .end while
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('while (x > 0)',    lines.pop(0))
        self.assertEqual('    if (x == 5)',  lines.pop(0))
        self.assertEqual('        break;',   lines.pop(0))
        self.assertEqual('    else',         lines.pop(0))
        self.assertEqual('    end if;',      lines.pop(0))
        self.assertEqual('    x = (x - 1);', lines.pop(0))
        self.assertEqual('end while;',       lines.pop(0))
        
    @rsl2xtuml.translate_docstring
    def test_for_each_loop(self, m):
        '''.//
        .select many a_set from instances of A
        .assign x = 0
        .for each a in a_set
            .assign x = x + 1
        .end for
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('select many a_set from instances of A;', lines.pop(0))
        self.assertEqual('x = 0;',                                 lines.pop(0))
        self.assertEqual('for each a in a_set',                    lines.pop(0))
        self.assertEqual('    x = (x + 1);',                       lines.pop(0))
        self.assertEqual('end for;',                               lines.pop(0))
        
    @rsl2xtuml.translate_docstring
    def test_for_loop_with_break(self, m):
        '''.//
        .select many a_set from instances of A
        .assign x = 0
        .for each a in a_set
            .if (x == 3)
                .break for
            .end if
            .assign x = x + 1
        .end for
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('select many a_set from instances of A;', lines.pop(0))
        self.assertEqual('x = 0;',                                 lines.pop(0))
        self.assertEqual('for each a in a_set',                    lines.pop(0))
        self.assertEqual('    if (x == 3)',                        lines.pop(0))
        self.assertEqual('        break;',                         lines.pop(0))
        self.assertEqual('    else',                               lines.pop(0))
        self.assertEqual('    end if;',                            lines.pop(0))
        self.assertEqual('    x = (x + 1);',                       lines.pop(0))
        self.assertEqual('end for;',                               lines.pop(0))

    @rsl2xtuml.translate_docstring
    def test_first_in_loop(self, m):
        '''.//
        .select many a_set from instances of A
        .for each a in a_set
            .if (first a_set)
                .break for
            .end if
        .end for
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('select many a_set from instances of A;', lines.pop(0))
        self.assertEqual('for each a in a_set',                    lines.pop(0))
        self.assertEqual('    if (/* first */ empty a_set)',       lines.pop(0))
        self.assertEqual('        break;',                         lines.pop(0))
        self.assertEqual('    else',                               lines.pop(0))
        self.assertEqual('    end if;',                            lines.pop(0))
        self.assertEqual('end for;',                               lines.pop(0))
    
    @rsl2xtuml.translate_docstring
    def test_not_first_in_loop(self, m):
        '''.//
        .select many a_set from instances of A
        .for each a in a_set
            .if (not_first a_set)
                .break for
            .end if
        .end for
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('select many a_set from instances of A;', lines.pop(0))
        self.assertEqual('for each a in a_set',                    lines.pop(0))
        self.assertEqual('    if (/* not_first */ empty a_set)',   lines.pop(0))
        self.assertEqual('        break;',                         lines.pop(0))
        self.assertEqual('    else',                               lines.pop(0))
        self.assertEqual('    end if;',                            lines.pop(0))
        self.assertEqual('end for;',                               lines.pop(0))
        
    @rsl2xtuml.translate_docstring
    def test_last_in_loop(self, m):
        '''.//
        .select many a_set from instances of A
        .for each a in a_set
            .if (last a_set)
                .break for
            .end if
        .end for
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('select many a_set from instances of A;', lines.pop(0))
        self.assertEqual('for each a in a_set',                    lines.pop(0))
        self.assertEqual('    if (/* last */ empty a_set)',        lines.pop(0))
        self.assertEqual('        break;',                         lines.pop(0))
        self.assertEqual('    else',                               lines.pop(0))
        self.assertEqual('    end if;',                            lines.pop(0))
        self.assertEqual('end for;',                               lines.pop(0))
        
    @rsl2xtuml.translate_docstring
    def test_not_last_in_loop(self, m):
        '''.//
        .select many a_set from instances of A
        .for each a in a_set
            .if (not_last a_set)
                .break for
            .end if
        .end for
        '''
        s_sync = m.select_any('S_SYNC')
        lines = s_sync.Action_Semantics_internal.splitlines()
        self.assertEqual('select many a_set from instances of A;',  lines.pop(0))
        self.assertEqual('for each a in a_set',                     lines.pop(0))
        self.assertEqual('    if (/* not_last */ empty a_set)',     lines.pop(0))
        self.assertEqual('        break;',                          lines.pop(0))
        self.assertEqual('    else',                                lines.pop(0))
        self.assertEqual('    end if;',                             lines.pop(0))
        self.assertEqual('end for;',                                lines.pop(0))
        

if __name__ == '__main__':
    import logging
    logging.basicConfig()
    unittest.main()

