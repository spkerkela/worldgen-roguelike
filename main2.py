from engine.game import Game
from engine.generators.name_generator import NameGenerator

name_generator = NameGenerator('engine/generators/seednames/greek_gods')
name = name_generator.new_name()
game = Game('The Dungeons of ' + name, 'spkerkela', 80, 80)
game.start()
