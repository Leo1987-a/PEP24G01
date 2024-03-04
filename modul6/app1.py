#import Magazin as m
class Magazin:
    stoc = {}
    user_input = None

    def modificare_stoc(self):
        print('''Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire''')
        self.user_input = input('Ce alegeti:') # o alta varianta care se poate face direct fara a fii declarat mai sus
        if self.user_input == '2':
            produs,pret,stoc = input('give product, price ,stoc ').split(',')
            self.adauga_produs(produs,pret,stoc)
            self.adauga_produs('unt', 8, 100)
            self.adauga_produs('iaurt', 3, 320)
            self.adauga_produs('paine', 6, 5)
    def adauga_produs(self, produs, pret, stoc):  # functile acestea se mai numesc si metode
        self.stoc.update({produs: (pret, stoc)})
#       if self.stoc.produs < '10':
#            print('Comanda produs')
    def set_status(self,status):
        self.status = status

    def show_stock(self):
        print(self.stoc)

    def start(self):
        print('''Meniu:
        1. Vizualizare stoc
        2. Adaugare produs
        3. Stergere produs
        4. Iesire''')
        while input('Ce alegeti:') !='4':
            if self.user_input == '2':
                produs, pret, stoc = input('give product, price ,stoc ').split(',')
                self.adauga_produs(produs, pret, stoc)
            elif self.user_input == '1':
                self.show_stock()
            elif self.user_input=='2':
                pass
            self.user_input= input((f'Ce alegeti:\n'))

#o alta forma de a scrie
m=Magazin()
Magazin.adauga_produs(m,'unt',5, 100)
m.adauga_produs('unt',5,100)


m.status =open
# m = Magazin()
m.modificare_stoc()
print(f'Ai ales: {m.user_input}')
# m.adauga_produs('unt',8, 100)  #fiecare adaugare se va modifica si sus la produse
print(m.stoc)
print(m.show_stock())
