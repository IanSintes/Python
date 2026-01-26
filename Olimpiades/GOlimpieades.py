c = int(input())
for _ in range(c):
    m,n = map(int, input().split())
    temps = []

    for i in range(m):
        s = 0
        for x in map(int, input().split()):
            s += x
            temps.append((s,i))

    temps.sort()

    penalitzacio = [0]*m
    k = 0
    i = 0

    while i < len(temps):
        j = i
        # Busquem tots els enviaments amb el mateix temps
        while j < len(temps) and temps[j][0] == temps[i][0]:
            j += 1

        # Apliquem la penalitcacio amb el mateix k
        for p in range(i,j):
            t,est = temps[p]
            penalitzacio[est] += t *k
        
        k += (j - i)
        i = j
    print("".joun(map(str, penalitzacio)))