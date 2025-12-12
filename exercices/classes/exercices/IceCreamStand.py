from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """classe pour modeliser un stand de glace"""
    def __init__(self, flavors):
        self.flavors = flavors
    def get_flavors(self):
        for flavor in self.flavors:
            return flavor


stand_1  = IceCreamStand(["rouge","vert","bleu"])
print(stand_1.get_flavors())