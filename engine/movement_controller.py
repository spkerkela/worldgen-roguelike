from component import Component
from world import Tiletypes

class MovementController(Component):
	"""A component to move entities"""
	def move(self, dx, dy, dz = 0):
		world = self.owner.world

		# Move to location if it is not blocked
		if not world.is_blocked(self.owner.x + dx, self.owner.y + dy, self.owner.z + dz):
			self.owner.x += dx
			self.owner.y += dy
			self.owner.z += dz
		else:
			self.dig(self.owner.x + dx, self.owner.y + dy, self.owner.z + dz)


		entity = world.entity_at(self.owner.x + dx, self.owner.y + dy, self.owner.z + dz) 
		if entity and entity != self.owner:
			print self.owner.name + " attacks " + entity.name
			entity.get_component('stats').cur_hp -= 5

	def dig(self, x, y, z):
		world = self.owner.world
		stats = self.owner.get_component('stats')
		if world.in_bounds(x, y, z) and world.tile_at(x,y,z).blocks and stats.cur_energy > 0:
			world.set_tile_at(x,y,z, Tiletypes['floor'])
			stats.cur_energy -= 1

	def rest(self):
		stats = self.owner.get_component('stats')
		if stats.cur_energy < stats.max_energy:
			stats.cur_energy += 1