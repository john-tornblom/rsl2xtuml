#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestEmit(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def testEmitHelloWorld(self, rc):
        '''Hello world
        .emit to file "testfile"'''
        lines = rc.splitlines()
        self.assertEqual('TMPL::append(text: "Hello world" + "\\n");', lines.pop(0))
        self.assertEqual('TMPL::emit(filename: "testfile");', lines.pop(0))
    
    @rsl2xtuml.translate_docstring    
    def testEmitWithoutLinebreak_Case1(self, rc):
        '''Hello\
        world'''
        self.assertEqual('TMPL::append(text: "Hello        world" + "\\n");', rc)
        



if __name__ == '__main__':
    unittest.main()

