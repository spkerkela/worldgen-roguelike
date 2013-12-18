import random
from name_generator import NameGenerator

# dictionary to tie cultures
godnames_dict = {
    "finnish" : "finnish_gods",
    "egyptian" : "egyptian_gods",
    "greek" : "greek_gods",
    "roman" : "roman_gods",
    "norse" : "norse_gods"
}

# Gods have elements they control, they are listed here
# maybe an idea to generate them too?

elements = [
    "fire","water","air","nature",
    "earth","electricity","death",
    "life"]

class GodGenerator(object):
    def __init__(self, godnames_key):
        self.name_generator = NameGenerator('seednames/' + 
                                            godnames_dict[godnames_key])

    def new_god(self):
        name = self.name_generator.new_name()
        powers = random.sample(elements, 3)
        description = "All hail the new god {}," \
                      "who wields the power of {} and {}!".format(name,
                                                                powers[1],
                                                                powers[2])
        
        #print "All hail the new god " + name + ", who wields the
        #power of " + powers[0] +", " + powers[1] +" and " + powers[2]
        #+ "!"
        print description

if __name__ == '__main__':
    gg = GodGenerator("roman")
    gg.new_god()
