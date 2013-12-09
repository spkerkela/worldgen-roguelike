from component import Component

class Stats(Component):
    """Stats like str, int etc"""
    def __init__(self, name, max_hp, max_mana, intellect, strength, agility, energy):
        super(Stats, self).__init__(name)
        self.max_hp = max_hp
        self.cur_hp = max_hp
        self.max_mana = max_mana
        self.cur_mana = max_mana
        self.cur_energy = energy
        self.max_energy = energy

        # Base stats
        
        self.intellect = intellect
        self.strength = strength
        self.agility = agility
