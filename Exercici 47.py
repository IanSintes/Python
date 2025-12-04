def eliminarcapicua(llista):
    if len(llista) <= 2:
        return []
    return llista[1:-1]

print(eliminarcapicua([1, 2, 3, 4, 5]))
print(eliminarcapicua([10, 20, 30]))
print(eliminarcapicua([7, 8]))
print(eliminarcapicua([9]))
