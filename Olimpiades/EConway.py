def pestat(t, f, c):
n = int(input())
for _ in range(n):
    f,c = map(int, input().split())
    tauler=[list(e.input().split())for e in range(f)]
    for _ in range(f):
        a = input().split()
        tauler.append(a)
    resultat = pestat(tauler, f, c)
    for e in resultat:
        print("").join
