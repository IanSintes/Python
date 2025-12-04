def hi_ha_duplicats(llista):
    vist = set()
    for element in llista:
        if element in vist:
            return True
        vist.add(element)
    return False

print(hi_ha_duplicats([1, 2, 3, 4, 5]))
print(hi_ha_duplicats([1, 2, 3, 2, 5]))
print(hi_ha_duplicats(['a', 'b', 'c']))
print(hi_ha_duplicats(['a', 'b', 'a']))
print(hi_ha_duplicats([]))