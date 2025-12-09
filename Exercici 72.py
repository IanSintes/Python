import os

directori = "/home/ian/AO/Prova"
os.makedirs(directori, exist_ok=True)

os.chdir(directori)

companys = ["Ian", "Izan", "Lucas", "Rafa"]
with open("Ex12.txt", "w", encoding="utf-8") as f:
    for nom in companys:
        f.write(nom + "\n")

professors = ["Sr. Joan", "Sra. Belen"]
with open("Ex12.txt", "a", encoding="utf-8") as f:
    for nom in professors:
        f.write(nom + "\n")

llista_noms = []
with open("Ex12.txt", "r", encoding="utf-8") as f:
    for linia in f:
        llista_noms.append(linia.strip())

print("Llista completa de noms:", llista_noms)