import libtcodpy as lbt

class Item(object):
    """an item that can be used upto uses times,
    if uses is None, can be used indefinitely"""
    def __init__(self,
                 name,
                 char,
                 effects=[],
                 color=lbt.white,
                 level=1,
                 uses=None):
        self.name = name
        self.char = char
        self.color = color
        self.uses = uses
        self.effects = effects
        self.level = level

    def use(self, owner, target=None):
        if not target:
            _target = owner
        else:
            _target = target
        if self.effects:
            for effect in self.effects:
                target.apply_effect(effect)
        print "{} used {}".format(_target.name, self.name)
        if self.uses:
            self.uses -= 1
