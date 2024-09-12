class Position:
	def __init__(self, row: int, column: int):
		self.row = row
		self.column = column
	def __repr__(self):
		return
	
	def __str__(self):
		return
	
	def __eq__(self, other) :
		if isinstance(other, Position):
			return self.row == other.row and self.column == other.column
		return False
	def __hash__(self) :
		return hash((self.row, self.column))
	def add(self, other):
		return Position(self.row + other.row, self.column + other.column)
	def subtract(self, other):
		return Position(self.row - other.row, self.column - other.column)