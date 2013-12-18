from component import Component

class AttackComponent(Component):
    
    def __init__(self, name, attack):
        super(AttackComponent, self).__init__(name)
        self.attack_value = attack

    def attack(self, target):
        destructible = target.get_component("destructible")
        if not destructible:
            return
        else:
            print "{} attacks {}".format(self.owner.name,
                                         target.name)
            print "attack", "defense"
            print self.attack_value, destructible.defense
            damage = max(self.attack_value - destructible.defense,
                         0)
            destructible.take_damage(damage)
