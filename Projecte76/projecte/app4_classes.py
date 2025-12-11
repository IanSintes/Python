# app4_classes.py

class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parlar(self):
        return "Fa un soroll."

class Gos(Animal):
    def parlar(self):
        return "Guau guau!"

class Gat(Animal):
    def parlar(self):
        return "Mèu!"

def objectes_polimorfisme():
    print("\n--- APLICACIÓ 4: Objectes i polimorfisme ---")

    animals = [
        Gos("Tobbie"),
        Gat("Luna"),
        Animal("Criatura misteriosa")
    ]

    print("\nCada animal parla diferent:")
    for a in animals:
        print(f"{a.nom}: {a.parlar()}")

