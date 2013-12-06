import random

god_seeds = ["finnish","egyptian","greek", "roman","norse"]

# Markov chains from roguebasin!
class Mdict:
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)  

class MName:
    """
    A name from a Markov chain
    """
    def __init__(self, seed_names, chainlen = 2 ):
        """
        Building the dictionary
        """
        if chainlen > 10 or chainlen < 1:
            print "Chain length must be between 1 and 10, inclusive"
            sys.exit(0)
 
        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen

        for l in seed_names:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")
 
    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()

class NameGenerator:
    def __init__(self, names_filename):
        #self.sourcepath = ''.join(['seednames/',names_filename])
        self.sourcepath = names_filename
    
    def new_name(self, n=1):
        names = []
        try:
            with open(self.sourcepath) as f:
                # gets rid of all whitespace this way
                content = ''.join(f.read().split())
                names = content.split(',')
                f.close()   
        except IOError, e:
            print e
            print "Cannot open " + self.sourcepath
            return
        
        markov_gen = MName(names)

        if n <= 1:
            return markov_gen.New()
        else:
            returnlist = []
            for x in xrange(1,n):
                returnlist.append(markov_gen.New().strip())
            return returnlist

def main():
    # for some fun testing
    god_generator = NameGenerator('seednames/egyptian_gods')

    gods = god_generator.new_name(50)


    for x in gods:
        print x

    #for orc in orcnames:
    #   print orc

if __name__ == '__main__':
    main()