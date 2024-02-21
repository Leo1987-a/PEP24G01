# . Creati un script care sa calculeze valoarea lui x = 3x^2 - 4y + 4 in intervalul 10,20,
# unde y = 3x.
# Creati o functie pentru calcularea lui x si y.
# Sample output:
# ============= X = 10 ==================
# Rezultatul functiei: 184
# ============= X = 11 ==================
# Rezultatul functiei: 235
# ============= X = 12 ==================
# Rezultatul functiei: 292
# ============= X = 13 ==================
# Rezultatul functiei: 355
# …


#Dam valoarea minima lui x=10 iar cea maxima este egala cu 20.
#Folosim functia while pentru a afisa valorile lui x pana la valoarea maxima 20.
#Alocam valorii y, valoarea care a fost data in enunt y=3*x.iar dupa aceea vom apela printu cu textul dorit.Printam rezultatul ecuatiei dar in cadrul functiei vom adauga fiecarul x care urmeaza +1
#x = (3*x**2 -4*y+4)  care rezulta in (3*x**2-4*3*x+4)
x=10
while x <=20:
  y=3*x
  print("============ X =",x,"=============")
  print("Rezultatul functiei:", 3*x**2-4*y+4)
  x+=1
