import libtcodpy as lbt
from renderer import Renderer
from message_system import MessageSystem

class Game:
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

		# List of game objects (entities)
		self.entities = []

		self.player = None

	def add_entity(self, entity, is_player=False, add_as_message_receiver=True):
		self.entities.append(entity)
		if add_as_message_receiver:
			self.message_system.register(entity)

		# Allow entities to access the main Game instance
		entity.game = self

		if is_player:
			self.player = entity

	def update(self):
		mouse = lbt.Mouse()
		key = lbt.Key()
		lbt.sys_check_for_event(lbt.EVENT_KEY_PRESS|lbt.EVENT_MOUSE, key, mouse)

		if not key.vk == lbt.KEY_NONE:
			pass
		
		self.message_system.propagate_messages()
		
		# update entities
		for e in self.entities:
			e.update()

	def draw(self):
		lbt.console_clear(self.con)

		for e in self.entities:
			e.draw(self.con)

		lbt.console_blit(self.con, 0, 0, self.screen_width, 
					 self.screen_height, 0, 0, 0)
		lbt.console_flush()

	def start(self):
		while not lbt.console_is_window_closed():
			self.update()
			self.draw()