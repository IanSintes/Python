def es_primer(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prims = []
for num in range(1, 101):
    if es_primer(num):
        prims.append(num)

print("Nombres primers entre 1 i 100:", prims)
print("Total de nombres primers:", len(prims))