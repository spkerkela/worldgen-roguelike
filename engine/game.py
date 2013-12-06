import libtcodpy as lbt
from renderer import Renderer
from input_system import InputSystem
from message_system import MessageSystem
from screen import PlayScreen, StartScreen
from world import World

class Game(object):
	def __init__(self, name, author=None, screen_width=80, screen_height=50,
				 fps=60):
		self.name = name
		self.author = author
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.fps = fps

		# Initialization of systems here
		self.message_system = MessageSystem()

		# Initialization of libtcod here
		lbt.console_init_root(self.screen_width,self.screen_height, self.name, False)
		self.con = lbt.console_new(self.screen_width, self.screen_height)
		lbt.sys_set_fps(self.fps)

		# Initialization of renderer
		self.renderer = Renderer(self.con)

		# Initialization of input
		self.input_system = InputSystem()

		# List of game objects (entities)
		self.entities = []

		self.player = None

		# Screens
		self.screen = StartScreen(self)


	def add_entity(self, entity, is_player=False, add_as_message_receiver=True):
		self.entities.append(entity)
		if add_as_message_receiver:
			self.message_system.register(entity)

		# Allow entities to access the main Game instance
		entity.game = self

		if is_player:
			self.player = entity

	def update(self):
		# get new input
		self.input_system.update()
		self.screen.handle_input()

		#if not self.input_system.key.vk == lbt.KEY_NONE:
		#	self.message_system.send_message(str(self.input_system.key.vk))
		
		self.message_system.send_message("hey")
		self.message_system.propagate_messages()
		
		# update entities
		for e in self.entities:
			e.update()

	def draw(self):
		lbt.console_clear(self.con)

		self.screen.draw(self.con)

		lbt.console_blit(self.con, 0, 0, self.screen_width, 
					 self.screen_height, 0, 0, 0)
		lbt.console_flush()

	def start(self):
		self.draw() # initial draw!
		while not lbt.console_is_window_closed():
			self.update()
			self.draw()

	def is_blocked(self, x, y):
		
		if not self.in_bounds(x, y):
			return True

		if self.entity_at(x, y):
			return True

		return False

	def in_bounds(self, x, y):
		return x < self.screen_width and x >= 0 and y < self.screen_height and y >= 0

	def entity_at(self, x, y):
		for e in self.entities:
			if e.x == x and e.y == y:
				return e