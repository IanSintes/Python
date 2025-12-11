# main.py

from app1_llistes import treball_llistes
from app2_fitxers import treball_fitxers
from app3_jocs import jugar
from app4_classes import objectes_polimorfisme
from app5_bigdata import aplicacio_bigdata
from app6_web import iniciar_web

def main():
    while True:
        print("\n--- Projecte 76: Selecciona una aplicació ---")
        print("1: Llistes i números aleatoris")
        print("2: Fitxers (agenda)")
        print("3: Joc")
        print("4: Objectes i polimorfisme")
        print("5: Big data / Scraping")
        print("6: Servei web")
        print("0: Sortir")

        opcio = input("Opció: ")

        if opcio == "1":
            treball_llistes()
        elif opcio == "2":
            treball_fitxers()
        elif opcio == "3":
            jugar()
        elif opcio == "4":
            objectes_polimorfisme()
        elif opcio == "5":
            aplicacio_bigdata()
        elif opcio == "6":
            iniciar_web()
        elif opcio == "0":
            print("Fins aviat!")
            break
        else:
            print("Opció incorrecta.")

if __name__ == "__main__":
    main()

