# 1 Exercici
"""
a = input("Escriu el teu nom: ")
print("Hola, {}".format(a))
"""
# 2 Exercici
"""
a = input("Escriu el teu nom: ")
b = len(a)
print("Hola, {}, Tens {} caracters ".format(a,b))
"""
# 3 Exercici
"""
def fvocals(a):
    num=0
    for e in a:
        if e in "aeiouAEIOUàáèéìíòóùúÀÁÈÉÌÍÒÓÙÚ":
            num = num + 1
    return num
a = input("Escriu el teu nom: ")
b = len(a)
c = fvocals(a)
print("Hola, {}, Tens {} caracters, {} vocals ".format(a,b,c))
"""
# 4 Exercici
"""
a = input("Escriu el teu nom: ")
b = "No"
if "a" in a:
    b="Si"
print("Hola, {}, Tens {} caracters i {} te la lletra A ".format(a,len(a),b))
"""
# 5 Exercici
"""
a = input("Escriu el teu nom: ")
b = "No"
if "a" in a or "e" in a or "i" in a or "o" in a or "o" in a:
    b="Si"
print("Hola, {}, Tens {} caracters i {} te una vocal minim ".format(a,len(a),b))
"""
# 1 Exercici EDAT
"""
edat = int(input("Escriu la teva edat: "))
print("Hola, tens {} anys".format(edat))
"""
# 2 Exercici EDAT
"""
edat = int(input("Escriu la teva edat: "))
if edat>18:
    print("Ets major d'edat")
elif edat<18:
    print("Ets menor d'edat")
else:
    print("Tens 18 justos")
print("Hola, tens {} anys".format(edat))
"""
# 3 Exercici EDAT
"""
edat = int(input("Escriu la teva edat: "))
if edat>18:
    print("Ets major d'edat")
elif edat<18:
    print("Ets menor d'edat")
else:
    print("Tens 18 anys justos")
if edat%2==0:
    print("La teva edat es parell")
else:
    print("La teva edat es senar")
print("Hola, tens {} anys".format(edat))
"""
# 4 Exercici EDAT
"""
edat = int(input("Escriu la teva edat: "))
if edat>18:
    print("Ets major d'edat")
elif edat<18:
    print("Ets menor d'edat")
else:
    print("Tens 18 anys justos")
if edat%2==0:
    print("La teva edat es parell")
else:
    print("La teva edat es senar")
if edat%5==0:
    print("La teva edat es multiple de 5")
else:
    print("La teva edat no es multiple de 5")
print("Hola, tens {} anys".format(edat))
"""
# 5 Exercici EDAT
edat = int(input("Escriu la teva edat: "))
if edat>18:
    print("Ets major d'edat")
elif edat<18:
    print("Ets menor d'edat")
else:
    print("Tens 18 anys justos")
if edat%2==0:
    print("La teva edat es parell")
else:
    print("La teva edat es senar")
if edat%5==0:
    print("La teva edat es multiple de 5")
else:
    print("La teva edat no es multiple de 5")
if edat in range(0,11):
    print("La teva edat esta entre 0-10")
elif edat in range(11,21):
    print("La teva edat esta entre 11-20")
else:
    print("La teva edad es major de 20")

    print("Hola, tens {} anys".format(edat))
