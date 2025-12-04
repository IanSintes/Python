def index_paraula(llista, paraula):
    for i, p in enumerate(llista):
        if p == paraula:
            return i
    return -1

paraules = ["Anna", "Lucas", "Ian", "Pere", "Ramon"]
paraules.sort()
print(paraules)  

print(index_paraula(paraules, "Ian"))
print(index_paraula(paraules, "Lucas"))
print(index_paraula(paraules, "Izan"))