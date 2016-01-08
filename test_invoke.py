#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml

from xtuml import where_eq as where


class TestInvoke(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_invoke_without_arguments(self, m):
        '.invoke f()'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         '::f();')
        
    @rsl2xtuml.translate_docstring
    def test_invoke_with_dot_in_name(self, m):
        '.invoke module.f()'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual('::module_f();', 
                         s_sync.Action_Semantics_internal)

    @rsl2xtuml.translate_docstring
    def test_invoke_with_return_value(self, m):
        '.invoke res = f()'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual('res = ::f();',
                         s_sync.Action_Semantics_internal)

    @rsl2xtuml.translate_docstring
    def test_invoke_with_parameter(self, m):
        '''.//
        .function f
            .param integer x
        .end function
        .invoke f(1)
        .//'''
        s_sync = m.select_any('S_SYNC', where(Name='test_invoke_with_parameter'))
        self.assertEqual(s_sync.Action_Semantics_internal,
                         '::f(x: 1);')

    @rsl2xtuml.translate_docstring
    def test_parameter_order(self, m):
        '''.//
        .function f
            .param integer x
            .param boolean y
            .param string z
        .end function
        .invoke f(1, true, "s")
        .//'''
        s_sync = m.select_any('S_SYNC', where(Name='test_parameter_order'))
        self.assertEqual(s_sync.Action_Semantics_internal,
                         '::f(x: 1, y: true, z: "s");')



if __name__ == '__main__':
    unittest.main()
