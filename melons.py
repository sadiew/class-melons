
class AbstractMelonOrder(object):

    def get_base_price(self):
        return 5.0


class WatermelonOrder(AbstractMelonOrder):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""       

        total = self.get_base_price() * qty

        if qty >= 3:
            total = total * 0.75

        return total

class CantaloupeOrder(AbstractMelonOrder):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty
        
        if qty >= 5:
            return total * 0.5
        else:
            return total

class CasabaOrder(AbstractMelonOrder):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        price = self.get_base_price() + 1        

        total = price * qty

        if self.imported == True:
            total = total * 1.5

        return total

class SharlynOrder(AbstractMelonOrder):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty

        if self.imported == True:
            total = total * 1.5
        
        return total

class SantaClausOrder(AbstractMelonOrder):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty

        if self.imported == True:
            total = total * 1.5
        
        return total

class ChristmasOrder(AbstractMelonOrder):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty

        return total

class HornedMelonOrder(AbstractMelonOrder):
    species = "HornedMelon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty

        if self.imported == True:
            total = total * 1.5
        
        return total

class XiguaOrder(AbstractMelonOrder):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""    
        
        if self.shape == "square":
            price = self.get_base_price() * 2

        total = price * qty

        if self.imported == True:
            total = total * 1.5
        
        return total

class OgenOrder(AbstractMelonOrder):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        price = self.get_base_price() + 1        
        
        total = price * qty

        return total