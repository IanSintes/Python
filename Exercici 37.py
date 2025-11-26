import random
import time

def intro():
    print ("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
""")

def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

def trobada(canviTalaiot):
    print ("T'estas apropant al talaiot...")
    time.sleep(1)
    print ("Està fosc i és tenebrós...")
    time.sleep(1)
    print ("Un gran gegant salta davant teu, t'agafa i ...\n")
    time.sleep(1)
    gegantamic = random.randint(1, 2)
    if canviTalaiot == str(gegantamic):
        print ("Et convida a menjar!")
        return True
    else:
        print ("Se't menja d'un mos...ÑAMÑAMÑAM")
        return False

# Funció principal amb punts
partidaNova = "si"

while partidaNova.lower() in ("s", "si"):
    intro()
    punts = 0
    while True:
        nTalaiot = canviTalaiot()
        if trobada(nTalaiot):
            punts += 1
            print(f"Punts acumulats: {punts}\n")
            continuar = input("Vols intentar un altre talaiot? (si/no): ")
            if continuar.lower() not in ("s", "si"):
                print(f"Final del joc! Has aconseguit {punts} punts.\n")
                break
        else:
            print(f"Has perdut! Has aconseguit {punts} punts.\n")
            break

    partidaNova = input("Vols tornar a jugar? Introdueixi si o no: ")
    print("\n")