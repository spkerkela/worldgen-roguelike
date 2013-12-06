import libtcodpy as lbt
import random
class Tile(object):
	"""Tiles are the terrain that entities walk on"""
	def __init__(self, char, blocks = False, blocks_sight = False, color=lbt.dark_green):
		self.blocks = blocks
		self.blocks_sight = blocks_sight
		self.char = char
		self.color = color
		

class World(object):
	"""The world object contains all entities and items and map info"""
	def __init__(self, width, height, depth):
		self.width = width
		self.height = height
		self.depth = depth
		# random.choice(['.','#',',','='])
		self.tiles = [[[Tile(random.choice(['.',',','`'])) for _ in xrange(width)]
		for _ in xrange(height)] for _ in xrange(depth)]
		
		# entities
		self.player = None
		self.entities = []

	def tile_at(self, x, y, z):
		return self.tiles[z][y][x]

	def is_blocked(self, x, y, z):
		if not self.in_bounds(x, y, z):
			return True

		if self.entity_at(x,y,z):
			return True

		return self.tile_at(x, y, z).blocks

	def in_bounds(self, x, y, z):
		return x < self.width and x >= 0 and y < self.height and y >= 0 and z < self.depth and z >= 0

	def entity_at(self, x, y, z):
		for e in self.entities:
			if e.x == x and e.y == y and e.z == z:
				return e

	def char_at(self, x, y , z):
		e = self.entity_at(x, y, z)

		if e:
			return e.char
		else:
			return self.tile_at(x, y, z).char

	def color_at(self, x, y, z):
		e = self.entity_at(x, y, z)

		if e:
			return e.color
		else:
			return self.tile_at(x, y, z).color

	def add_entity(self, entity, is_player=False, add_as_message_receiver=True):
		self.entities.append(entity)

		# Allow entities to access the world
		entity.world = self
		# Allow entities to access the game's systems
		entity.game = self.screen.game

		if is_player:
			self.player = entity

		if add_as_message_receiver:
			self.screen.game.message_system.register(entity)