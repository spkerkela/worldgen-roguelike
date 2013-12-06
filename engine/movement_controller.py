from component import Component

class MovementController(Component):
	"""A component to move entities"""
	def move(self, dx, dy, dz = 0):
		world = self.owner.world

		# Move to location if it is not blocked
		if not world.is_blocked(self.owner.x + dx, self.owner.y + dy, self.owner.z + dz):
			self.owner.x += dx
			self.owner.y += dy
			self.owner.z += dz

		entity = world.entity_at(self.owner.x + dx, self.owner.y + dy, self.owner.z + dz) 
		if entity and entity != self.owner:
			print self.owner.name + " attacks " + entity.name
			entity.get_component('stats').cur_hp -= 5