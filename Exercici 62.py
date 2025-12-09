from functools import reduce

def passar_a_numero(llista):
    return reduce(lambda x, y: x * 10 + y, llista)

# Proves
print(passar_a_numero([3, 4, 1, 5]))
print(passar_a_numero([1, 0, 0]))
print(passar_a_numero([9, 2]))