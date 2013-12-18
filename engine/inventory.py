from component import Component

class Inventory(Component):
    
    def __init__(self, name, size):
        super(Inventory, self).__init__(name)
        self.size = size
        self.items = []

    def put_item(self, item):
        if len(self.items) < self.size:
            self.items.append(item)
            self.owner.world.remove_item(item)
    
    def take_item(self, index):
        item = self.items[index]
        self.items[index] = None
        return item
