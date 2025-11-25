def llegir_frase(a):
#Prec: Donat un nombre
#Post: Retorna una llista de n-element llegits del teclat
    llista = list()
    for i in range(n):
        llista.append(input(""))
    return llista

def escriure_frase(llista):
#Prec: Donada una llista d'elements
#Post: Imprimeix cada element de la llista
    for e in llista:
        print(e)

def convertir_majuscula(s):
    vocal="aeiouAEIOU"
    llista = list(s)
    for i,e in enumerate(s):
        if e not in vocal:
            llista[i]=e.upper()
    return"".join(llista)

#Programa principal
n = int(input("Escriu una frase:"))
llista = llegir_frase(n)
for i,e in enumerate(llista):
    llista[i]=convertir_majuscula
escriure_frase(llista)