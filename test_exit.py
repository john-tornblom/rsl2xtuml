#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestExit(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_exit_status(self, m):
        '.exit 1'
        s_sync = m.select_any('S_SYNC')
        self.assertEqual(s_sync.Action_Semantics_internal,
                         'ARCH::exit(status: 1);')
        

if __name__ == '__main__':
    unittest.main()

