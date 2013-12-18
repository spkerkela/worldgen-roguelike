import libtcodpy as lbt

class InputSystem(object):
    """System for handling input"""
    def __init__(self):
        self.key = None
        self.mouse = None

    def update(self):
        self.mouse = lbt.Mouse()
        self.key = lbt.Key()
        lbt.sys_wait_for_event(lbt.EVENT_KEY_PRESS|lbt.EVENT_MOUSE,
                               self.key, 
                               self.mouse,
                               True)
