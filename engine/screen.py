import libtcodpy as lbt
import gui
from world import World
from entity import Entity
from stats import Stats
from fov import FovComponent
from movement_controller import MovementController
from ai import PlayerAi, SimpleFollowAi
import generators.world_generator as worldgen
import copy
import random

class Screen(object):
    def __init__(self, game):
        self.game = game
        self.subscreen = None

    def draw(self, con):
        pass

    def handle_input(self):
        pass

    def add_subscreen(self, subscreen):
        self.subscreen = subscreen
        subscreen.parent = self

class StartScreen(Screen):
    """The screen first shown when the game starts"""
    def __init__(self, game):
        super(StartScreen, self).__init__(game)

    def draw(self, con):
        lbt.console_print_ex(con, lbt.console_get_width(con) / 2, lbt.console_get_height(con) / 2, lbt.BKGND_NONE, lbt.CENTER, "Start the game by pressing enter!")

    def handle_input(self):
        if self.game.input_system.key.vk == lbt.KEY_ENTER:
            self.game.screen = PlayScreen(50, 50, self.game)

class LoseScreen(Screen):
    """A screen to show when the player loses"""
    def __init__(self, game):
        super(LoseScreen, self).__init__(game)

    def draw(self, con):
        lbt.console_print_ex(con, lbt.console_get_width(con) / 2, lbt.console_get_height(con) / 2, lbt.BKGND_NONE, lbt.CENTER, "You have lost! Press enter to restart!")

    def handle_input(self):
        if self.game.input_system.key.vk == lbt.KEY_ENTER:
            self.game.screen = PlayScreen(50, 50, self.game)
        
        

class PlayScreen(Screen):
    """The default playing screen"""
    def __init__(self, width, height, game):
        super(PlayScreen, self).__init__(game)
        self.screen_width = width
        self.screen_height = height
        #self.world = worldgen.create_empty_world(width * 2, height * 2, 1)
        self.world = worldgen.create_cavernous_world(width * 2, height * 2, 1)
        self.world.screen = self
        self.w_console = lbt.console_new(self.screen_width, self.screen_height)
        self.game = game
        self.add_entities()
        self.world.update_fov()
        self.world.compute_fov()

    def add_entities(self):

        base_stats = Stats("stats", 100, 80, 5, 6, 7, 10)
        
        player = Entity(int(self.world.width / 2),
                int(self.world.height / 2), 0,
                '@', "player")
        player.add_component(MovementController("controller"))
        player.add_component(PlayerAi("ai"))
        player.add_component(copy.deepcopy(base_stats))
        player.add_component(FovComponent("fov"))

        self.world.add_entity(player, is_player=True)
        # must be done in this order!
        player.get_component("fov").initialize()

        monster_count = 4
        for x in xrange(0, monster_count):
            m = Entity(random.randint(0, self.game.screen_width),
                       random.randint(0, self.game.screen_height),
                       0, 'm', 'monster', lbt.yellow)
            m.add_component(MovementController("controller"))
            m.add_component(SimpleFollowAi("ai"))
            m.add_component(copy.deepcopy(base_stats))
            self.world.add_entity(m)

    def get_scroll_x(self):
        return max(0, min(self.world.player.x - self.screen_width / 2, self.world.width - self.screen_width))

    def get_scroll_y(self):
        return max(0, min(self.world.player.y - self.screen_height / 2, self.world.height - self.screen_height))

    def handle_input(self):
        if self.game.input_system.key.vk == lbt.KEY_ESCAPE:
            self.game.screen = LoseScreen(self.game)
        for e in self.world.entities:
            e.update()
        if self.world.player.get_component('stats').cur_hp <= 0:
            self.game.screen = LoseScreen(self.game)


    def draw(self, con):
        lbt.console_clear(self.w_console)
        lbt.console_print_frame(con, 0, 0, self.screen_width+2, self.screen_height+2, fmt="Game world")
        self.draw_gui(con)
        self.draw_world(self.get_scroll_x(), self.get_scroll_y())

        if self.subscreen:
            self.subscreen.draw(con)

        lbt.console_blit(self.w_console, 0, 0,
                         self.screen_width,
                         self.screen_height,
                         con, 1, 1)

    def draw_world(self, left, top):
        p = self.world.player
        fov = p.get_component("fov")
        for x in xrange(self.screen_width):
            for y in xrange(self.screen_height):
                wx = x + left
                wy = y + top
                if fov.can_see(wx, wy, p.z):
                    lbt.console_put_char_ex(self.w_console,
                                            x, y,
                                            self.world.char_at(wx, wy, p.z),
                                            self.world.color_at(wx, wy, p.z),
                                            lbt.black)


    def draw_gui(self, con):
        plr = self.world.player
        gui.print_entity_stats(con, plr, 1, self.screen_height + 3)
        gui.print_location_info(con, 20, self.screen_height + 3, self.world.tile_at(plr.x, plr.y, plr.z))
