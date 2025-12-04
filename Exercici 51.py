def elimina_duplicats(llista):
    nova_llista = []
    vist = set()
    for element in llista:
        if element not in vist:
            nova_llista.append(element)
            vist.add(element)
    return nova_llista

print(elimina_duplicats([1, 2, 3, 2, 4, 1, 5]))
print(elimina_duplicats(['a', 'b', 'a', 'c']))
print(elimina_duplicats([1, 1, 1, 1]))
print(elimina_duplicats([]))