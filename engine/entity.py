import libtcodpy as lbt

class Entity(object):
	"""This is a generic game-entity: the player,
	a monster, an item, the stairs.."""
	def __init__(self, x, y, z, char, name, color=lbt.white):
		self.x = x
		self.y = y
		self.z = z
		self.char = char
		self.name = name
		self.components = {}
		self.count = 10
		self.color = color

	def update(self):
		# Update components if they have update
		for c in self.components.values():
			if 'update' in dir(c):
				c.update()

	def receive_message(self, message):
		pass

	def add_component(self, component):
		self.components[component.name.lower()] = component
		component.owner = self

	def get_component(self, component_name):
		"""Return the component if it exists,
		else None. Ignores string case"""
		return self.components.get(component_name.lower(), None)

	def set_component(self, component_name, component):
		if not self.get_component(component_name):
			print "No component '" + component_name + "' found"
		else:
			self.components[component_name.lower()] = component
			component.owner = self

	def remove_component(self, component_name):
		"""Remove the component if it exists,
		ignores string case"""
		name = component_name.lower()
		if self.get_component(name):
			del self.components[name]