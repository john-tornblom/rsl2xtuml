#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestExit(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_exit_status(self, s):
        '.exit 1'
        self.assertEqual('ARCH::exit(status: 1);', s)
        

if __name__ == '__main__':
    unittest.main()

