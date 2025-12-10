# Fitxers
l = [50,100,200]
with open("Prova.txt","w") as f:
    f.write(str(l))
with open("Prova.txt","r") as f:
    linias = f.readlines()
    linias = [n[:-1] for n in linias]
    print(linias)

"""
f = open("Prova.txt","r")
print(f.read())
f.close()


with open("Prova.txt","r") as f:
    linias = f.readlines()
    linias = [n[:-1] for n in linias]
    print(linias)
    """