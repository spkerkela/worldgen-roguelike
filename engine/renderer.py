import libtcodpy as lbt

class Renderer:
	def __init__(self, console):
		self.console = console

	def draw_entity(self, entity):
		lbt.console_set_char(self.console, entity.x, entity.y, entity.char)
		