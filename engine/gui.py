import libtcodpy as lbt
import string_utils
import copy

def print_entity_stats(con, entity, x, y):
    stats = entity.get_component('stats')
    if not stats:
        return
    stats_y = y
    lbt.console_print(con, x, stats_y, entity.name.capitalize())
    lbt.console_print(con, x, stats_y + 1, 
                      "HP : " + str(stats.cur_hp))
    lbt.console_print(con, x, stats_y + 2,
                      "MP : " + str(stats.cur_mana))
    lbt.console_print(con, x, stats_y + 3,
                      "Strength : " + str(stats.strength))
    lbt.console_print(con, x, stats_y + 4,
                      "Intellect : " + str(stats.intellect))
    lbt.console_print(con, x, stats_y + 5, 
                      "Agility : " + str(stats.agility))
    lbt.console_print(con, x, stats_y + 6,
                      "Energy : " + str(stats.cur_energy))
    lbt.console_print(con, x, stats_y + 7,
                      "Location : {}, {}".format(entity.x,
                                                 entity.y))

def print_location_info(con, x, y, tile):
    lbt.console_print(con, x, y, tile.char + " - " + tile.name)

def print_inventory(con, entity, x, y):
    inventory = entity.get_component("inventory")
    if not inventory:
        return
    
    name = string_utils.genetive(entity.name.capitalize())
    lbt.console_print(con, x, y,
                      "{} inventory".format(name))
    for i in xrange(len(inventory.items)):
        item = inventory.items[i]
        ichar = item.char
        iname = item.name
        line = copy.deepcopy("{} {} {}".format(i+1, ichar, iname))
        lbt.console_print(con,
                          x,
                          y + i + 1,
                          line)
