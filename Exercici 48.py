def esta_ordenada(llista):
    if all(llista[i] <= llista[i+1] for i in range(len(llista)-1)):
        return "Està ordenada de forma ascendent"
    elif all(llista[i] >= llista[i+1] for i in range(len(llista)-1)):
        return "Està ordenada de forma descendent"
    else:
        return "No està ordenada"

print(esta_ordenada([3, 2, 1]))
print(esta_ordenada([4, 5, 6]))
print(esta_ordenada([1, 3, 2]))
print(esta_ordenada([7]))