def mostra(a):
    for e in a:
        print(e)
    for i,e in enumerate(a):
        a[i]=e*2
    return a

a=[2, 3, 4]
mostra(a)
print(a)