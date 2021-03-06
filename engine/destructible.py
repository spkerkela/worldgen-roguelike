import libtcodpy as lbt
from component import Component
from item import Item
import copy
import gui 
class DestructibleComponent(Component):
    
    def __init__(self, name, defense):
        super(DestructibleComponent, self).__init__(name)
        self.defense = defense
    def take_damage(self, amount):
        stats = self.owner.get_component("stats")
        if amount > 0:
            msg = "{} takes {} damage".format(self.owner.name,
                                          amount)
            stats.cur_hp -= amount
            if stats.cur_hp <= 0:
                self.die()
        else:
            msg = "{} shrugs the attack off".format(self.owner.name)
        gui.message(msg)

    def die(self):
        world = self.owner.world
        if not self.owner == world.player:
            corpse = Item("{} corpse".format(self.owner.name),
                          chr(37),
                          color=lbt.red)
            world.add_item(corpse, 
                           self.owner.x,
                           self.owner.y,
                           self.owner.z)
            world.entities.remove(self.owner)
            self.owner.components = {}
