from component import Component

class TickerComponent(Component):
    """Component that calls a function it is given every update"""
    def __init__(self, name, func):
        Component.__init__(self,name)
        self.func = func

    def update(self):
        self.func()

class CounterComponent(Component):
    """A counter that starts at init_value (default 0)
    and increments or decrements to end_value by increment_amount (default 1)
    every update. An optional callback is called when
    end_value is reached"""
    
    def __init__(self, name, end_value,
                init_value=0, increment_amount=1,
                callback=None):
        Component.__init__(self,name)
        self.init_value = init_value
        self.end_value = end_value
        self.increment_amount = abs(increment_amount)
        self.callback = callback
        self.current_value = self.init_value
        if self.end_value < self.init_value:
            self.increment_amount *= (-1)

    def update(self):
        self.current_value = self.current_value + self.increment_amount
        print self.current_value

        ascending = self.increment_amount > 0

        if (ascending and self.current_value >= self.end_value) or (not ascending and self.current_value <= self.end_value):
            # Stop incrementing when goal reached
            self.increment_amount = 0
            if self.callback:
                self.callback()
                print self.owner.name

