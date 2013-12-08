import libtcodpy as lbt
import random
class Tile(object):
	"""Tiles are the terrain that entities walk on"""
	def __init__(self, chars, name, blocks = False, blocks_sight = False, color=lbt.dark_green):
		self.blocks = blocks
		self.blocks_sight = blocks_sight
		self.char = random.choice(chars)
		self.color = color
		self.name = name

Tiletypes = {
	'floor' : Tile(['.',',','`'], 'floor', color=lbt.darkest_grey),
	'wall' : Tile(['#'], 'wall', blocks=True, blocks_sight=True, color=lbt.dark_grey),
	'water' : Tile(['~'], 'water', blocks=True, color=lbt.blue)
}

class World(object):
	"""The world object contains all entities and items and map info"""
	def __init__(self, width, height, depth):
		self.width = width
		self.height = height
		self.depth = depth
		# entities
		self.player = None
		self.entities = []

	def tile_at(self, x, y, z):
		return self.tiles[z][y][x]

	def set_tile_at(self, x, y, z, tile):
		self.tiles[z][y][x] = tile

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

	def neighbors8(self, x, y, z):
		neighbors = []
		for xs in xrange(-1,2):
			for ys in xrange(-1,2):
				summed_x = x + xs
				summed_y = y + ys
				if summed_x == x and summed_y == y:
					pass
				elif summed_x < 0 or summed_x >= self.width or summed_y < 0 or summed_y >= self.height:
					pass
				else:
					neighbors.append(self.tile_at(summed_x, summed_y, z))
		# print len(neighbors)
		return neighbors