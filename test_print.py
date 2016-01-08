#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestPrint(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_print(self, m):
        '.print "Hello world"'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'LOG::LogInfo(message: "Hello world");')


if __name__ == '__main__':
    unittest.main()

