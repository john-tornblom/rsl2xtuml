#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestInfo(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def testVersion(self, m):
        '.assign x = "${info.Interpreter_Version}"'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = INFO::interpreter_version();')

    @rsl2xtuml.translate_docstring
    def testPlatform(self, m):
        '.assign x = "${info.interpreter_platform}"'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'x = INFO::interpreter_platform();')
        

if __name__ == '__main__':
    unittest.main()

