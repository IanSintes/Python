d = {'examen':9, 'tasca1':5,'tasca2':6}
l = d.items() #passa a llista
print(l)
y= dict(sorted(l,key=lambda x:x[1]),reverse=True)
print(y)


"""
l=['hola', 'casa', 'metge','cadira']
y = sorted(l,key=lambda x:x.count('a'),reverse=True)
print(y)


x = (lambda x:x.count('a'))("Hola guapa, Que fas avui?")
print(x)

l = [3, 5, 4, 2]
x = reduce(lambda n1,n2:n1+n2,l)
print(x)

l=[3,25,8,9]
x = list(map(filter a>0, l))
print(x)

l=[3,25,8,9]
x = list(map(lambda x:x+10, l))
print(x)
"""