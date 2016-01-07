#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestInvoke(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_invoke_without_arguments(self, rc):
        '.invoke f()'
        self.assertEqual('::f();', rc)
        
    @rsl2xtuml.translate_docstring
    def test_nvoke_with_dot_in_name(self, rc):
        '.invoke module.f()'
        self.assertEqual('::module_f();', rc)

    @rsl2xtuml.translate_docstring
    def test_invoke_with_return_value(self, rc):
        '.invoke res = f()'
        self.assertEqual('res = ::f();', rc)

    @rsl2xtuml.translate_docstring
    def test_invoke_with_parameter(self, rc):
        '''.//
        .function f
            .param integer x
        .end function
        .invoke f(1)
        .//'''
        self.assertEqual('::f(x: 1);', rc)

    @rsl2xtuml.translate_docstring
    def testParameterOrder(self, rc):
        '''.//
        .function f
            .param integer x
            .param boolean y
            .param string z
        .end function
        .invoke f(1, true, "s")
        .//'''
        self.assertEqual('::f(x: 1, y: true, z: "s");', rc)



if __name__ == '__main__':
    unittest.main()
