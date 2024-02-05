'''a = 5.
b = 5
c = "ana"
d = a,b,c
# afisare locatie in memorie

print(id(d))
print(type(d))'''

a = 5.
b = 5
c = "ana"

print(f"""Location for a is: {hex(id(a))}
Location for b is: {hex(id(b))}
Location for c is: {hex(id(c))}""")

print(f"""
Type of a: {type(a)}
Type of b: {type(b)}
Type of c: {type(c)}""")