import libtcodpy as lbt
from engine.game import Game
from engine.entity import Entity
import random

name = "Wargrand"
game = Game('Warlords of ' + name, 'spkerkela', 80, 80)
player = Entity(40, 25, '@')

for x in xrange(1,10):
	m = Entity(random.randint(0,game.screen_width),
			   random.randint(0,game.screen_height), 'm')
	game.add_entity(m)

game.add_entity(player, is_player=True)

game.start()