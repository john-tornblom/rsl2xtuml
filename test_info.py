#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestInfo(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def testVersion(self, rc):
        '.assign x = "${info.Interpreter_Version}"'
        self.assertEqual('x = INFO::interpreter_version();', rc)

    @rsl2xtuml.translate_docstring
    def testPlatform(self, rc):
        '.assign x = "${info.interpreter_platform}"'
        self.assertEqual('x = INFO::interpreter_platform();', rc)
        

if __name__ == '__main__':
    unittest.main()

