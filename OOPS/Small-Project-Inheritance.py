# Multiple Inheritance

class MainFactory:
    def __init__(self,material,zips):
        self.material = material
        self.zips - zips

class BhopalFactory(MainFactory):
    def __init__(self, material, zips, colors):
        super().__init__(material, zips) # super() method points MainFactory
        self.colors = colors

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, colors, pockets):
        super().__init__(material, zips, colors) # super() method points BhopalFactory
        self.pockets = pockets

