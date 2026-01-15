n = int(input())
for i in range(n):
    s = input()
    x = s.split
    l = []
    resultat = True
    for e in x:
        if e!="0":
            l.append(int(e))
    pila = []
    if len(l)%2==1:
        resultat = False
    else:
        for e in l:
            if e > 0:
                pila.append(e)
            else:
                if not pila or pila[-1] != -e:
                    resultat = False
                    break
                pila.pop()
    if pila:
        resultat = False
    if resultat:
        print("Normal")
    else:
        print("PARANORMAL")