#!/usr/bin/env python
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestIntrinsics(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_get_env_var(self, m):
        '.invoke rc = GET_ENV_VAR("PATH")'
        self.fail('test case evaluation not implemented yet')

    @rsl2xtuml.translate_docstring
    def test_put_env_var(self, m):
        '.invoke rc = PUT_ENV_VAR("MY_PATH", "test")'
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_file_write(self, m):
        '.invoke rc = FILE_WRITE("/tmp/tempfile", "Hello world!")'
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_file_read(self, m):
        '.invoke rc = FILE_READ("/tmp/tempfile")'
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_shell_command(self, m):
        '.invoke rc = SHELL_COMMAND("true")'
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_integer_to_string(self, m):
        '.invoke rc = INTEGER_TO_STRING(1)'
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_real_to_string(self, m):
        '.invoke rc = REAL_TO_STRING(1.1)'
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_boolean_to_string(self, m):
        '.invoke rc = BOOLEAN_TO_STRING(False)'
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_string_to_integer(self, m):
        '.invoke rc = STRING_TO_INTEGER("1")'
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_string_to_real(self, m):
        '.invoke rc = STRING_TO_REAL("1.1")'
        self.fail('test case evaluation not implemented yet')
    

if __name__ == '__main__':
    unittest.main()
    
