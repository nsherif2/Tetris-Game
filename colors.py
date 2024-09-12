class Colors:
	dark_grey = (34, 40, 49)
	green = (34, 197, 94)
	red = (235, 87, 87)
	orange = (255, 159, 10)
	yellow = (252, 211, 77)
	purple = (155, 89, 182)
	cyan = (88, 214, 141)
	blue = (52, 152, 219)
	white = (255, 255, 255)
	dark_blue = (41, 128, 185)
	light_blue = (127, 179, 213)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
