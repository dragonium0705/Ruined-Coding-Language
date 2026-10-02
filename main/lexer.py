from enums.lexer import TokenType

class Lexer:
	def __init__(self, source):
		self.source = source 
		print(source)
		
	def parse(self):
		return self.source