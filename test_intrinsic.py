#!/usr/bin/env python3
# encoding: utf-8
# Copyright (C) 2016 John Törnblom

import unittest
import rsl2xtuml


class TestIntrinsics(unittest.TestCase):

    @rsl2xtuml.translate_docstring
    def test_GET_ENV_VAR(self, rc):
        '''
        .invoke rc = GET_ENV_VAR("PATH")
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')

    @rsl2xtuml.translate_docstring
    def test_GET_ENV_VAR_failure(self, rc):
        '''
        .invoke rc = GET_ENV_VAR("UNKNOWN_PATH")
        .exit rc.success
        '''
        self.fail('test case evaluation not implemented yet')

    @rsl2xtuml.translate_docstring
    def test_PUT_ENV_VAR(self, rc):
        '''
        .invoke rc = PUT_ENV_VAR("MY_PATH", "test")
        .exit rc.success
        '''
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_FILE_READ_WRITE(self, rc):
        '''
        .invoke rc = FILE_WRITE("/tmp/RSLTestCase", "Hello world!")
        .if ( not rc.success )
            .exit ""
        .end if
        .invoke rc = FILE_READ("/tmp/RSLTestCase")
        .if ( not rc.success )
            .exit ""
        .end if
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_FILE_READ_error(self, rc):
        '''
        .invoke rc = FILE_READ("/")
        .exit rc.success
        '''
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_FILE_Write_error(self, rc):
        '''
        .invoke rc = FILE_WRITE("/", "TEST")
        .exit rc.success
        '''
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_SHELL_COMMAND_true(self, rc):
        '''
        .invoke rc = SHELL_COMMAND("true")
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_SHELL_COMMAND_false(self, rc):
        '''
        .invoke rc = SHELL_COMMAND("false")
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_INTEGER_TO_STRING(self, rc):
        '''
        .invoke rc = INTEGER_TO_STRING(1)
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_REAL_TO_STRING(self, rc):
        '''
        .invoke rc = REAL_TO_STRING(1.1)
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_BOOLEAN_TO_STRING(self, rc):
        '''
        .invoke rc = BOOLEAN_TO_STRING(False)
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_STRING_TO_INTEGER(self, rc):
        '''
        .invoke rc = STRING_TO_INTEGER("1")
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_STRING_TO_INTEGER_invalid(self, rc):
        '''
        .invoke rc = STRING_TO_INTEGER("test")
        '''
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_STRING_TO_INTEGER_with_spaces(self, rc):
        '''
        .invoke rc = STRING_TO_INTEGER(" 1 ")
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_STRING_TO_REAL(self, rc):
        '''
        .invoke rc = STRING_TO_REAL("1.1")
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
    
    @rsl2xtuml.translate_docstring
    def test_STRING_TO_REAL_invalid(self, rc):
        '''
        .invoke rc = STRING_TO_REAL("test")
        '''
        self.fail('test case evaluation not implemented yet')
        
    @rsl2xtuml.translate_docstring
    def test_STRING_TO_REAL_with_spaces(self, rc):
        '''
        .invoke rc = STRING_TO_REAL(" 1.1 ")
        .exit rc.result
        '''
        self.fail('test case evaluation not implemented yet')
        

if __name__ == '__main__':
    unittest.main()
    
