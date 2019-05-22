from llvmlite import ir, binding
from rply import ParserGenerator
from rply import LexerGenerator

class Lexer():

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):

        # Key Words
        self.lexer.add('PRINT', r'print')
        self.lexer.add('FOR', r'for')
        self.lexer.add('WHILE', r'while')
        self.lexer.add('IN', r'in')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('TRUE', r'true')
        self.lexer.add('FALSE', r'false')
        self.lexer.add('IF', r'if')
        self.lexer.add('AND', r'and')
        self.lexer.add('OR', r'or')
        self.lexer.add('NOT', r'not')
        self.lexer.add('RETURN', r'return')
        self.lexer.add('CONTINUE', r'continue')
        self.lexer.add('BREAK', r'break')
        self.lexer.add('IMPORT', r'import')
        self.lexer.add('NONE', r'None')
        self.lexer.add('DEF', r'def')

        # MISC
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('COLON', r'\:')
        self.lexer.add('BIGGER', r'\>')
        self.lexer.add('LESSER', r'\<')

        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULTI', r'\*')
        self.lexer.add('PERCENT', r'\%')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('DIVUP', r'\//')
        self.lexer.add('EQU', r'\=')

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Single Alphabet
        self.lexer.add('ALPHABET', r'[a-zA-Z]')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()

class Parser():

    def __init__(self):
        self.pg = ParserGenerator(
        ['PRINT', 'FOR', 'WHILE', 'IN', 'ELSE', 'TRUE', 'FALSE', 'IF',
        'AND', 'OR', 'NOT', 'RETURN', 'CONTINUE', 'BREAK', 'IMPORT',
        'NONE', 'DEF', 'OPEN_PAREN', 'CLOSE_PAREN', 'SEMI_COLON',
        'COLON', 'BIGGER', 'LESSER', 'SUM', 'SUB', 'MULTI', 'PERCENT',
        'DIV', 'DIVUP', 'EQU', 'NUMBER', 'ALPHABET']
        )

    def parse(self):
        @self.pg.production('program: PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])




class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())



text_input = """
    print(4 + 2 - 3);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
