def mcd(a, b):
    if b == 0:
        return a
    r = a % b
    return mcd(b, r)


sortir=False
while not sortir:
    v = [int(x) for x in input().split()]
    if v[0] == 0:
        sortir = True
    else:
        r = v[1] # El primer valor es el mcd
        for e in v[2:]:
            r = mcd(max(r,e), min(r, e))
        print(r)