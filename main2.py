import libtcodpy as lbt
from engine.game import Game
from engine.entity import Entity
from engine.movement_controller import MovementController
from engine.generators.name_generator import NameGenerator
from engine.util_components import TickerComponent, CounterComponent
from engine.ai import PlayerAi, RandomAi, SimpleFollowAi
from engine.stats import Stats
import copy
import random

name_generator = NameGenerator('engine/generators/seednames/greek_gods')
name = name_generator.new_name()
game = Game('The Dungeons of ' + name, 'spkerkela', 80, 80)
game.start()
