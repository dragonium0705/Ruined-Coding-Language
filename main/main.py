from lexer import Lexer

def ruined_compile(source):
	test = Lexer(source).parse()
	
ruined_compile("Hello\nWorld")