import libtcodpy as lbt
from ..world import World, Tile, Tiletypes
import random

def create_empty_world(width, height, depth, tiletype='grass'):
    world = World(width, height, depth)
    world.tiles = [[[Tiletypes[tiletype] for _ in xrange(width)]
        for _ in xrange(height)] for _ in xrange(depth)]
    return world

def create_cavernous_world(width, height, depth):
    world = create_empty_world(width, height, depth, 'wall')
    for x in xrange(0, world.width):
        for y in xrange(0, world.height):
            for z in xrange(0, world.depth):
                randnum = random.random()
                if randnum < 0.4:
                    world.tiles[z][y][x] = Tiletypes['floor']
                else:
                    world.tiles[z][y][x] = Tiletypes['wall']

    for x in xrange(1,3):
        world = cellular_automata(world)
    return world

def blocks_count(list_of_tiles):
    count = 0
    for t in list_of_tiles:
        if t.blocks:
            count += 1
    return count

def cellular_automata(world):
    copyworld = world

    for x in xrange(0, world.width):
        for y in xrange(0, world.height):
            for z in xrange(0, world.depth):
                count = blocks_count(world.neighbors8(x, y, z))
                if count < 4:
                    copyworld.tiles[z][y][x] = Tiletypes['floor']
                elif count > 5:
                    copyworld.tiles[z][y][x] = Tiletypes['wall']

    world = copyworld
    return world
                