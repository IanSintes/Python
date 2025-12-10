from functools import reduce
def add(x,y):
    return x+y
ln=[]
sortir = 'n'
while sortir!='s':
    numero = float(input("Introdueixi un numero: "))
    ln.append(numero)
    sortir= input("\n Vols sortir? (s/n)")

sumapositius=reduce(add, [n for n in ln if n>0])
sumanegatius=reduce(add, [n for n in ln if n<0])
print("""
      Suma de nombres positius {} 
      Suma de nombres negatius {} 
      Mitjana {}""".format(sumapositius,sumanegatius,(sumanegatius+sumapositius/len(ln))))



"""
sumapositius=0
sumanegatius=0
nombrenumeros=0
sortir = 'n'
while sortir!='s':
    numero = float(input("Introdueixi un numero: "))
    nombrenumeros+=1
    if numero>0:
        sumapositius+=numero
    else:
        sumapositius+=numero
    sortir= input("\n Vols sortir? (s/n)")

print('''
      Suma de nombres positius {} 
      Suma de nombres negatius {} 
      Mitjana {}'''.format(sumapositius,sumanegatius,(sumanegatius+sumapositius/nombrenumeros)))

p = ["joan","miquel","pere","maria"]
cpa = [pa.title() for pa in p]
print(cpa)
p = [i for i in range(1,11)]
print(p)
s = [1**(i-1) for i in range(20) if i%2==1]
print(s)
m = [2*i +1 for i in range(20)]
print(m)
"""