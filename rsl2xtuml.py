#!/usr/bin/env python
import functools
import sys
import logging
import types
import rsl
import xtuml.tools

from bridgepoint import ooaofooa
from xtuml import where_eq as where
from xtuml import navigate_one as one
from xtuml import relate


logger = logging.getLogger(__name__)
    

class ActionTranslation(xtuml.tools.Walker):

    def __init__(self, metamodel):
        xtuml.tools.Walker.__init__(self)
        self.m = metamodel
        self.scope_level = -1
        
    def enter_scope(self):
        self.scope_level += 1
        
    def leave_scope(self):
        self.scope_level -= 1
    
    def linebreak(self):
        return '\n' + '    ' * self.scope_level
    
    def parameters(self, function_name):
        s_sync = self.m.select_one('S_SYNC', where(Name=function_name))
        first_filt = lambda sel: not one(sel).S_SPARM[54, 'precedes']()
        s_sparm = one(s_sync).S_SPARM[24](first_filt)
        while s_sparm:
            yield s_sparm.Name
            s_sparm = one(s_sparm).S_SPARM[54, 'succeeds']()
        
    def join(self, node):
        return ''.join(self.accept(node))
    
    def default_accept(self, node, **kwargs):
        raise Exception('Unhandled node %s' % node)
    
    def accept_BodyNode(self, node):
        yield self.join(node.statement_list)
        
    def accept_StatementListNode(self, node):
        self.enter_scope()
        
        for stmt in node.statements:
            stmt = ''.join(self.accept(stmt))
            if stmt:
                yield self.linebreak()
                yield stmt
                yield ';'
            
        self.leave_scope()
        yield self.linebreak()
        
    def accept_WhileNode(self, node):
        yield 'while '
        yield self.join(node.cond)
        yield self.join(node.statement_list)
        yield 'end while'
    
    def accept_ForNode(self, node):
        yield 'for each %s ' % node.variable_name
        yield 'in %s' % node.set_name
        yield self.join(node.statement_list)
        yield 'end for'
        
    def accept_BreakNode(self, node):
        yield 'break'
        
    def accept_IfNode(self, node):
        yield 'if '
        yield self.join(node.cond)
        yield self.join(node.iftrue)
        
        yield self.join(node.elif_list)
        
        if node.iffalse:
            yield 'else'
            yield self.join(node.iffalse)
            yield 'end if'
        
    def accept_ElIfListNode(self, node):
        for elif_ in node.elifs:
            yield self.join(elif_)
        
    def accept_ElIfNode(self, node):
        yield 'elif '
        yield self.join(node.cond)
        yield self.join(node.statement_list)
        
    def accept_AssignNode(self, node):
        yield self.join(node.variable)
        yield ' = '
        yield self.join(node.expr)
        
    def accept_BinaryOpNode(self, node):
        yield '('
        yield self.join(node.left)
        yield ' %s ' % node.sign
        yield self.join(node.right)
        yield ')'
    
    def accept_UnaryOpNode(self, node):
        yield '('
        
        if node.sign in ['first', 'not_first', 'last', 'not_last']:
            logger.warning('unsupported unary operator %s' % node.sign)
            yield '/* '
            yield node.sign
            yield ' */ '
            yield 'empty '
        else:
            yield '%s ' % node.sign
            
        yield self.join(node.value)
        yield ')'
        
    def accept_VariableAccessNode(self, node):
        yield node.name
    
    def accept_FieldAccessNode(self, node):
        yield self.join(node.variable)
        yield '.'
        yield node.field
    
    def accept_IntegerValueNode(self, node):
        yield node.value
        
    def accept_RealValueNode(self, node):
        yield node.value
    
    def accept_StringValueNode(self, node):
        return '"%s"' % node.value
    
    def accept_StringBodyNode(self, node):
        if not node.values:
            yield '""'
        
        prefix = ''
        for value in node.values:
            yield prefix
            yield self.join(value)
            prefix = ' + '
            
    def accept_CreateNode(self, node):
        yield 'create object instance %s ' % node.variable_name
        yield 'of %s' % node.key_letter
        
    def accept_SelectAnyInstanceNode(self, node):
        yield 'select any %s ' % node.variable_name
        yield 'from instances of %s' % node.key_letter
        yield self.join(node.where)

    def accept_SelectManyInstanceNode(self, node):
        yield 'select many %s ' % node.variable_name
        yield 'from instances of %s' % node.key_letter
        yield self.join(node.where)
    
    def accept_SelectOneNode(self, node):
        yield 'select one %s related by ' % node.variable_name
        yield self.join(node.instance_chain)
        yield self.join(node.where)
                                                   
    def accept_SelectAnyNode(self, node):
        yield 'select any %s related by ' % node.variable_name
        yield self.join(node.instance_chain)
        yield self.join(node.where)
                                                   
    def accept_SelectManyNode(self, node):
        yield 'select many %s related by ' % node.variable_name
        yield self.join(node.instance_chain)
        yield self.join(node.where)
                                                   
    def accept_InstanceChainNode(self, node):
        yield self.join(node.variable)
        for nav in node.navigations:
            yield '->'
            yield self.join(nav)
    
    def accept_NavigationNode(self, node):
        yield node.key_letter
        yield '['
        yield self.join(node.relation)
        yield ']'
    
    def accept_RelationNode(self, node):
        yield node.rel_id
        if node.phrase:
            yield ".'%s'" % node.phrase
    
    def accept_WhereNode(self, node):
        if node.expr:
            yield ' where '
            yield self.join(node.expr)
    
    def accept_SubstitutionVariableNode(self, node):
        if node.formats:
            yield 'TMPL::transform(format: "'
            yield ''.join(node.formats)
            yield '", text: '
            
        yield self.join(node.expr)
        
        if node.formats:
            yield ')'    
    
    def accept_SubstitutionNavigationNode(self, node):
        yield self.join(node.variable)
        logger.warning('surpressing navigation in where clause')
        #yield '->'
        #yield from self.accept(node.navigation)
        
    def accept_PrintNode(self, node):
        yield 'LOG::LogInfo(message: '
        yield self.join(node.value_list)
        yield ')'
    
    def accept_LiteralListNode(self, node):
        yield 'TMPL::append(text: '
        
        if not node.literals:
            yield '""'
            
        for literal in node.literals:
            yield self.join(literal)
            yield ' + '
        
        yield '"\\n"'
        yield ')'
    
    def accept_LiteralNode(self, node):
        yield '"%s"' % node.value
    
    def accept_EmitNode(self, node):
        yield 'TMPL::emit(filename: '
        yield self.join(node.emit_filename)
        yield ')'
        
    def accept_ParseKeywordNode(self, node):
        yield 'TMPL::parse_keyword(value: '
        yield self.join(node.expr)
        yield ', keyword: '
        yield self.join(node.keyword)
        yield ')'
        
    def accept_ClearNode(self, node):
        yield 'TMPL::clear();'
    
    def accept_ExitNode(self, node):
        yield 'ARCH::exit(status: '
        
        if node.return_code:
            yield self.join(node.return_code)
        else:
            yield '0'
            
        yield ')'

    def accept_InvokeNode(self, node):
        function_name = node.function_name.replace('.', '_')
        args = self.accept(node.argument_list)
        params = self.parameters(function_name)
        
        if node.variable_name:
            yield '%s = ' % node.variable_name
        
        yield '::'
        yield function_name
        yield '('
        yield ', '.join([p + ': ' + a for a, p in zip(args, params)])
        yield ')'
        
    def accept_ArgumentListNode(self, node):
        for arg in reversed(node.arguments):
            yield self.join(arg)
            
    def accept_FunctionNode(self, node):
        pe_pe = self.m.new('PE_PE')
        s_sync = self.m.new('S_SYNC', Name=node.name.replace('.', '_'))
        relate(pe_pe, s_sync, 8001)

        prev = None
        for param in node.parameter_list.parameters:
            s_dt = self.m.select_one('S_DT', where(Name=param.type))
            s_sparm = self.m.new('S_SPARM', Name=param.name)
            
            relate(s_sparm, s_sync, 24)
            relate(s_sparm, s_dt, 26)
            relate(s_sparm, prev, 54, 'succeeds')
            
            prev = s_sparm
        
        t = ActionTranslation(self.m)
        strings = t.accept(node.statement_list)
        s_sync.Action_Semantics_internal = ''.join(strings).strip('\n ')
    
        yield ''
    
    
def translate_text(metamodel, s):
    t = ActionTranslation(metamodel)
    root = rsl.parse_text(s)
    strings = t.accept(root)
    return ''.join(strings).strip('\n ')


def translate_file(metamodel, filename):
    t = ActionTranslation(metamodel)
    root = rsl.parse_file(filename)
    strings = t.accept(root)
    return ''.join(strings).strip('\n ')


def translate_docstring(fn):
    '''
    decorator function for translating the docstring of a function
    from rsl to oal.
    '''
    @functools.wraps(fn)
    def wrapper(*args):
        m = ooaofooa.empty_model()
        
        pe_pe = m.new('PE_PE')
        s_sync = m.new('S_SYNC', Name=fn.__name__)
        relate(pe_pe, s_sync, 8001)
        
        s_sync.Action_Semantics_internal = translate_text(m, fn.__doc__)
        
        args = list(args)
        args.append(m)
        fn(*args)
        
    return wrapper


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    m = ooaofooa.empty_model()
    oal = translate_file(m, sys.argv[1])
    print (oal)
    
