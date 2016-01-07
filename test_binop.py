#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestBinOp(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def testPlus(self, rc):
        '.assign x = 1 + 1'
        self.assertEqual('x = (1 + 1);', rc)
        
    @rsl2xtuml.translate_docstring
    def testMinus(self, rc):
        '.assign x = 1 - 1'
        self.assertEqual('x = (1 - 1);', rc)

    @rsl2xtuml.translate_docstring
    def testUnaryMinus(self, rc):
        '.assign x = 1 - -1'
        self.assertEqual('x = (1 - (- 1));', rc)
        
    @rsl2xtuml.translate_docstring
    def testMult(self, rc):
        '.assign x = 2 * 2'
        self.assertEqual('x = (2 * 2);', rc)
        
    @rsl2xtuml.translate_docstring
    def testDiv(self, rc):
        '.assign x = 10 / 2'
        self.assertEqual('x = (10 / 2);', rc)
        
    @rsl2xtuml.translate_docstring
    def testLessTrue(self, rc):
        '.assign x = 0 < 1'
        self.assertEqual('x = (0 < 1);', rc)
        
    @rsl2xtuml.translate_docstring
    def testLessFalse(self, rc):
        '.assign x = 0 < 0'
        self.assertEqual('x = (0 < 0);', rc)
        
    @rsl2xtuml.translate_docstring
    def testLessEqTrue(self, rc):
        '.assign x = 1 <= 1'
        self.assertEqual('x = (1 <= 1);', rc)
        
    @rsl2xtuml.translate_docstring
    def testLessEqFalse(self, rc):
        '.assign x = 2 <= 1'
        self.assertEqual('x = (2 <= 1);', rc)
        
    @rsl2xtuml.translate_docstring
    def testNotEqFalse(self, rc):
        '.assign x = 1 != 1'
        self.assertEqual('x = (1 != 1);', rc)
    
    @rsl2xtuml.translate_docstring
    def testGreatEqFalse(self, rc):
        '.assign x = 1 >= 2'
        self.assertEqual('x = (1 >= 2);', rc)
        
    @rsl2xtuml.translate_docstring
    def testGreatEqTrue(self, rc):
        '.assign x = 3 >= 2'
        self.assertEqual('x = (3 >= 2);', rc)
        
    @rsl2xtuml.translate_docstring
    def testNotEqTrue(self, rc):
        '.assign x = 0 != 1'
        self.assertEqual('x = (0 != 1);', rc)
        
    @rsl2xtuml.translate_docstring
    def testEqFalse(self, rc):
        '.assign x = 0 == 1'
        self.assertEqual('x = (0 == 1);', rc)
        
    @rsl2xtuml.translate_docstring
    def testEqTrue(self, rc):
        '.assign x = 1 == 1'
        self.assertEqual('x = (1 == 1);', rc)
        
    @rsl2xtuml.translate_docstring
    def testGroupedBinOp(self, rc):
        '.assign x = (1 + 1)'
        self.assertEqual('x = (1 + 1);', rc)
        
    @rsl2xtuml.translate_docstring
    def testChainedBinOp(self, rc):
        '.assign x = (1 + 1) + 1'
        self.assertEqual('x = ((1 + 1) + 1);', rc)

    @rsl2xtuml.translate_docstring
    def testChainedUnaryOp(self, rc):
        '.assign x = not (1 == 1)'
        self.assertEqual('x = (not (1 == 1));', rc)

    @rsl2xtuml.translate_docstring
    def testAndBinOpTrue(self, rc):
        '.assign x = True and True'
        self.assertEqual('x = (True and True);', rc)
        
    @rsl2xtuml.translate_docstring
    def testAndBinOpFalse(self, rc):
        '.assign x = True and False'
        self.assertEqual('x = (True and False);', rc)
        
    @rsl2xtuml.translate_docstring
    def testOrBinOpTrue(self, rc):
        '.assign x = True or False'
        self.assertEqual('x = (True or False);', rc)
        
    @rsl2xtuml.translate_docstring
    def testOrBinOpWithoutSpaces(self, rc):
        '.assign x = (True)or(False)'
        self.assertEqual('x = (True or False);', rc)
        
    @rsl2xtuml.translate_docstring
    def testAndBinOpWithoutSpaces(self, rc):
        '.assign x = (True)AND(True)'
        self.assertEqual('x = (True and True);', rc)
        
    @rsl2xtuml.translate_docstring
    def testOrBinOpFalse(self, rc):
        '.assign x = False or False'
        self.assertEqual('x = (False or False);', rc)
    
    @rsl2xtuml.translate_docstring
    def testBinOpPipe(self, rc):
        '''.//
        .create object instance a1 of A
        .create object instance a2 of A
        .create object instance a3 of A
        .assign a1.Name = "A1"
        .assign a2.Name = "A2"
        .assign a3.Name = "A3"
        .//
        .select any a1_set from instances of A where (selected.Name == "A1")
        .select any a2_set from instances of A where (selected.Name == "A2")
        .//
        .assign a_set = a1_set | a2_set
        .assign x = cardinality a_set
        '''
        lines = rc.splitlines()
        self.assertEqual('create object instance a1 of A;', lines.pop(0))
        self.assertEqual('create object instance a2 of A;', lines.pop(0))
        self.assertEqual('create object instance a3 of A;', lines.pop(0))
        self.assertEqual('a1.Name = "A1";', lines.pop(0))
        self.assertEqual('a2.Name = "A2";', lines.pop(0))
        self.assertEqual('a3.Name = "A3";', lines.pop(0))
        self.assertEqual('select any a1_set from instances of A where (selected.Name == "A1");', lines.pop(0))
        self.assertEqual('select any a2_set from instances of A where (selected.Name == "A2");', lines.pop(0))
        self.assertEqual('a_set = (a1_set | a2_set);', lines.pop(0))
        self.assertEqual('x = (cardinality a_set);', lines.pop(0))
        
    @rsl2xtuml.translate_docstring
    def testBinOpAmpesand(self, rc):
        '''.//
        .create object instance a1 of A
        .create object instance a2 of A
        .create object instance a3 of A
        .assign a1.Name = "A1"
        .assign a2.Name = "A2"
        .assign a3.Name = "A3"
        .//
        .select any a1_set from instances of A where (selected.Name == "A1")
        .select any a2_set from instances of A where (selected.Name == "A2")
        .//
        .assign a_set = a1_set & a2_set
        .assign x = cardinality a_set
        '''
        lines = rc.splitlines()
        self.assertEqual('create object instance a1 of A;', lines.pop(0))
        self.assertEqual('create object instance a2 of A;', lines.pop(0))
        self.assertEqual('create object instance a3 of A;', lines.pop(0))
        self.assertEqual('a1.Name = "A1";', lines.pop(0))
        self.assertEqual('a2.Name = "A2";', lines.pop(0))
        self.assertEqual('a3.Name = "A3";', lines.pop(0))
        self.assertEqual('select any a1_set from instances of A where (selected.Name == "A1");', lines.pop(0))
        self.assertEqual('select any a2_set from instances of A where (selected.Name == "A2");', lines.pop(0))
        self.assertEqual('a_set = (a1_set & a2_set);', lines.pop(0))
        self.assertEqual('x = (cardinality a_set);', lines.pop(0))
        
    @rsl2xtuml.translate_docstring    
    def testInstancePlusInstance(self, rc):
        '''.//
        .create object instance a1 of A
        .create object instance a2 of A
        .assign a1.Name = "A1"
        .assign a2.Name = "A2"
        .//
        .assign a_set = a1 + a2
        .assign x = cardinality a_set
        '''
        lines = rc.splitlines()
        self.assertEqual('create object instance a1 of A;', lines.pop(0))
        self.assertEqual('create object instance a2 of A;', lines.pop(0))
        self.assertEqual('a1.Name = "A1";', lines.pop(0))
        self.assertEqual('a2.Name = "A2";', lines.pop(0))
        self.assertEqual('a_set = (a1 + a2);', lines.pop(0))
        self.assertEqual('x = (cardinality a_set);', lines.pop(0))
        
    @rsl2xtuml.translate_docstring
    def testInstanceMinusInstance(self, rc):
        '''.//
        .create object instance a1 of A
        .create object instance a2 of A
        .assign a1.Name = "A1"
        .assign a2.Name = "A2"
        .//
        .assign a_set = a1 - a2
        .assign x = cardinality a_set
        '''
        lines = rc.splitlines()
        self.assertEqual('create object instance a1 of A;', lines.pop(0))
        self.assertEqual('create object instance a2 of A;', lines.pop(0))
        self.assertEqual('a1.Name = "A1";', lines.pop(0))
        self.assertEqual('a2.Name = "A2";', lines.pop(0))
        self.assertEqual('a_set = (a1 - a2);', lines.pop(0))
        self.assertEqual('x = (cardinality a_set);', lines.pop(0))
    
    @rsl2xtuml.translate_docstring
    def testInstanceMinusSameInstance(self, rc):
        '''.//
        .create object instance a1 of A
        .assign a1.Name = "A1"
        .//
        .assign a_set = a1 - a1
        .assign x = cardinality a_set
        '''
        lines = rc.splitlines()
        self.assertEqual('create object instance a1 of A;', lines.pop(0))
        self.assertEqual('a1.Name = "A1";', lines.pop(0))
        self.assertEqual('a_set = (a1 - a1);', lines.pop(0))
        self.assertEqual('x = (cardinality a_set);', lines.pop(0))
        

if __name__ == '__main__':
    unittest.main()

