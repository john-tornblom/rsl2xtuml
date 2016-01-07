#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestSelect(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def testSelectAny(self, rc):
        '.select any a from instances of A'
        self.assertEqual('select any a from instances of A;', rc)

    @rsl2xtuml.translate_docstring        
    def testSelectMany_Empty(self, rc):
        '.select many a_set from instances of A'
        self.assertEqual('select many a_set from instances of A;', rc)
        
    @rsl2xtuml.translate_docstring
    def testSelectOneNavigation(self, rc):
        '.select one b related by a->B[R1]'
        self.assertEqual('select one b related by a->B[R1];', rc)

    @rsl2xtuml.translate_docstring
    def testSelectAnyNavigation(self, rc):
        '.select any b related by a->B[R1]'
        self.assertEqual('select any b related by a->B[R1];', rc)

    @rsl2xtuml.translate_docstring
    def testSelectManyNavigation(self, rc):
        '.select many b_set related by a->B[R1]'
        self.assertEqual('select many b_set related by a->B[R1];', rc)

    @rsl2xtuml.translate_docstring
    def testSelectOneReflexiveNavigation(self, rc):
        ".select one second_inst related by first_inst->A[R1.'next']"
        self.assertEqual("select one second_inst related by first_inst->A[R1.'next'];", rc)
        
    @rsl2xtuml.translate_docstring
    def testSelectAnySubstituionNavigation(self, rc):
        '.select any a from instances of A where ("${selected->B[R1].name}" == "Test")'
        self.assertEqual('select any a from instances of A where ("${selected->B[R1].name}" == "Test")', rc)
        
    @rsl2xtuml.translate_docstring
    def testSelectWithManySpaces(self, rc):
        '.select       any        a       from          instances       of      A'
        self.assertEqual('select any a from instances of A;', rc)

    @rsl2xtuml.translate_docstring
    def testSelectWithTypeName(self, rc):
        '.select any string from instances of A'
        self.assertEqual('select any string from instances of A;', rc)
        

if __name__ == '__main__':
    unittest.main()

