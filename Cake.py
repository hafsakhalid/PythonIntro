import random

class Cake(object):
    
    #constructor
    def __init__(self, name, ingreds, price): 
        self.name = name
        self.ingreds = ingreds
        if(len(ingreds) < 3): 
            raise ValueError("Please add more ingrediants")
        self.price = random.randint(10, 15)
    
    def __str__(self): 
        return self.name, round(self.price, 2)

    def isbetter(self, cake): 
        owningred = len(self.ingred)
        ownratio = self.price//owningred
        otheringred = len(cake.ingred)
        otherratio = cake.price//otheringred
        if(ownratio <= otherratio): 
            return True
        else: 
            return False








