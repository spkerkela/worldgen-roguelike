from component import Component
from world import Tiletypes

class MovementController(Component):
    """A component to move entities"""
    def move(self, dx, dy, dz = 0):
        world = self.owner.world

        # Move to location if it is not blocked
        if not world.is_blocked(self.owner.x + dx,
                                self.owner.y + dy, 
                                self.owner.z + dz):
            self.owner.x += dx
            self.owner.y += dy
            self.owner.z += dz
        else:
            self.dig(self.owner.x + dx,
                     self.owner.y + dy,
                     self.owner.z + dz)


        entity = world.entity_at(self.owner.x + dx,
                                 self.owner.y + dy, 
                                 self.owner.z + dz) 
        attacker = self.owner.get_component("attack")
        if (entity and 
            entity != self.owner and
            attacker):
            #print self.owner.name + " attacks " + entity.name
            attacker.attack(entity)

    def dig(self, x, y, z):
        world = self.owner.world
        stats = self.owner.get_component('stats')
        tile = world.tile_at(x,y,z)
        if (world.in_bounds(x, y, z) and
            tile.blocks and
            tile.diggable and 
            stats.cur_energy > 0):
            world.set_tile_at(x,y,z, Tiletypes['floor'])
            stats.cur_energy -= 1

    def rest(self):
        stats = self.owner.get_component('stats')
        if stats.cur_energy < stats.max_energy:
            stats.cur_energy += 1

    def grab(self):
        o = self.owner
        item = o.world.item_at(o.x, o.y, o.z) 
        if item and o.get_component("inventory"):
            o.get_component("inventory").put_item(item)
