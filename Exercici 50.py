import random

def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]

def hi_ha_duplicats(llista):
    vist = set()
    for element in llista:
        if element in vist:
            return True
        vist.add(element)
    return False

# Creem la llista
llista = llista_20_elements()
print("Llista generada:", llista)

# Comprovem duplicats
if hi_ha_duplicats(llista):
    print("Hi ha elements duplicats.")
else:
    print("No hi ha elements duplicats.")
