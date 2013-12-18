import libtcodpy as lbt
from component import Component

class FovComponent(Component):
    """for fov checks"""
    def __init__(self, name):
        super(FovComponent, self).__init__(name)
    
    def initialize(self):
        self.world = self.owner.world
        self.fov_map = self.world.fov_map
        self.visible = [[False for _ in xrange(self.world.height)] 
                        for _ in xrange(self.world.width)]

    def can_see(self, x, y, z):
        e = self.owner
        # Break out early if we are not on the same level
        if not e.z == z:
            return False
        lbt.map_compute_fov(self.fov_map, e.x, e.y, 10)
        return lbt.map_is_in_fov(self.fov_map, x, y)
