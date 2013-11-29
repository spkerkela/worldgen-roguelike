import libtcodpy as lbt

class Entity:
	"""This is a generic game-entity: the player, a monster, an item, the stairs.."""
	def __init__(self, x, y, char):
		self.x = x
		self.y = y
		self.char = char

	def update(self):
		pass

	def draw(self, con):
		lbt.console_set_char(con, self.x, self.y, self.char)

	def receive_message(self, message):
		print self.char + " received message: " + message

	#def add_component(self, component):
