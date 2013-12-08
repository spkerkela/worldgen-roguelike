from component import Component
import random

class AI(Component):
	"""Ai component that handles the AI of the entity"""
	def __init__(self, name):
		super(AI, self).__init__(name)

class PlayerAi(AI):
	"""player AI is special, it uses input and requires
	that the owner has a movement controller"""
	def __init__(self, name):
		super(PlayerAi, self).__init__(name)
	
	def update(self):
		#print self.owner.name + " is thinking.."
		key = self.owner.game.input_system.key
		move_controller = self.owner.get_component('controller')
		dx, dy = 0, 0
		key_char = chr(key.c)

		if key_char == 's':
			dy = 1
		elif key_char == 'w':
			dy = -1
		elif key_char == 'd':
			dx = 1
		elif key_char == 'a':
			dx = -1

		elif key_char == 'r':
			move_controller.rest()

		if not (dx == 0 and dy == 0):
			move_controller.move(dx, dy)

class RandomAi(AI):
	"""Randomly wanders around"""
	def __init__(self, name):
		super(RandomAi, self).__init__(name)

	def update(self):
		dx = random.randint(-1,1)
		dy = random.randint(-1,1)
		self.owner.get_component('controller').move(dx, dy)

class SimpleFollowAi(AI):
	def __init__(self, name):
		super(SimpleFollowAi, self).__init__(name)

	def update(self):
		player = self.owner.world.player
		dx = 0
		dy = 0
		if self.owner.x > player.x:
			dx = -1
		elif self.owner.x < player.x:
			dx = 1
		if self.owner.y > player.y:
			dy = -1
		elif self.owner.y < player.y:
			dy = 1

		self.owner.get_component('controller').move(dx, dy)