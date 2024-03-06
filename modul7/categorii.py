class Categorii():
    def __init__(self,nume,pret,stoc):
        self.nume = nume
        self.pret = pret
        self.stoc = stoc

class Haine(Categorii):
    pass
class Accesorii(Categorii):
    pass

class Incltaminte(Categorii):
    pass

# tricouri = Haine("Tricou",20,35)
# print(tricouri.__class__.__name__)
# print(type(tricouri))
class Incaltaminte:
    pass