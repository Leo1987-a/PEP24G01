import random

print(random.choice(['p','f','h']))

nume_p= input('Introdu un nume:')
optiune = {'p':'piatra','f':'foarfeca','h':'hartie','q':'renunta'}
optiuni_afisate=str()

for key,value in optiune.items():
    optiuni_afisate +=(f'{key},({value})')
# input(f'Introduceti optiunea,{optiune} ')

# #combinations ={(rock,paper):False,(paper,rock):True,
#                (rock,scissors):True,(scissors,rock):False,
#                (paper,scissors):False,(scissors,paper):True}

optiuni_player = input(f'Alege optiunea : [{optiuni_afisate}')
optiuni_server = list(optiune.keys())
optiuni_server.remove('q')
optiuni_server = random.choice(optiuni_server)
print(f'> {nume_p}: {optiune[optiuni_player]}')
print(f'> Server :{optiune[optiuni_server]}')

if optiuni_server == 'p' and optiuni_player== 'f':
    print('Serverul a castigat')
elif  optiuni_server == 'f' and optiuni_player== 'h':
    print('Serverul a castigat')
elif optiuni_server == 'h' and optiuni_player== 'p':
    print('Playerul  a castigat')
elif optiuni_server == "f" and optiuni_player == "h":
    print("Serverul a castigat")
elif optiuni_server == optiuni_player:
    print("Egalitate")

else:
    print(nume_p, "A castigat")



