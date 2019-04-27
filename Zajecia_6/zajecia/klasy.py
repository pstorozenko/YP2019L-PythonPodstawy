from math import sqrt

class Punkt:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    
    def wypisz_punkt(self):
        print("Jestem punktem:")
        print(self.x, self.y)
    
    def odleglosc_od(self, drugi_punkt):
        dx = self.x - drugi_punkt.x
        dy = self.y - drugi_punkt.y
        return sqrt(dx**2 + dy**2)
    
    def __repr__(self):
        s = "Punkt (" + str(self.x) + ", " + str(self.y) + ")"
        return s

p0 = Punkt(0, 0)
p1 = Punkt(3, 4)

p0.wypisz_punkt()
p1.wypisz_punkt()
print(p0.odleglosc_od(p1))
print(p0)