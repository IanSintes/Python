from abc import ABC, abstractmethod

# EXERCICI 73.1
# Classe abstracta Animal

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    # Mètode abstracte
    @abstractmethod
    def xerrar(self):
        pass

    # Mètode abstracte
    @abstractmethod
    def mourem(self):
        pass

    # Mètode comú
    def quisoc(self):
        print(f"Som un {self.especie} i tenc {self.edat} anys")

# Subclasses d’Animal

class Cavall(Animal):
    def __init__(self, edat):
        super().__init__("Cavall", edat)

    def xerrar(self):
        print("Hiiii")

    def mourem(self):
        print("Corrent")

class Dofi(Animal):
    def __init__(self, edat):
        super().__init__("Dofí", edat)

    def xerrar(self):
        print("Clicks")

    def mourem(self):
        print("Nadant")

# EXERCICI 73.2
# Abella amb mètode extra picar

class Abella(Animal):
    def __init__(self, edat):
        super().__init__("Abella", edat)

    def xerrar(self):
        print("Bzzz")

    def mourem(self):
        print("Volant")

    def picar(self):
        print("Pica!")

# EXERCICI 73.3
# Humà amb atribut nom

class Huma(Animal):
    def __init__(self, nom, edat):
        super().__init__("Humà", edat)
        self.nom = nom

    def xerrar(self):
        print("Hola")

    def mourem(self):
        print("Caminant")

    def quisoc(self):
        print(f"Som {self.nom}, un humà de {self.edat} anys")

# EXERCICI 73.4
# Fiet amb atribut pares i mètode nompares

class Fiet(Huma):
    def __init__(self, nom, edat, pares):
        super().__init__(nom, edat)
        self.pares = pares

    def nompares(self):
        print("Pares:", ", ".join(self.pares))

# EXERCICI 73.1
# Centaure (herència múltiple: Cavall i Humà)

class Centaure(Cavall, Huma):
    def __init__(self, nom, edat):
        Animal.__init__(self, "Centaure", edat)
        self.nom = nom

    def xerrar(self):
        print("Soc mig humà i mig cavall")

    def mourem(self):
        print("Galopant i caminant")

# EXERCICI 73.1
# Classe Xou (sense relació amb Animal)

class Xou:
    def xerrar(self):
        print("Xerrant al xou")

    def mourem(self):
        print("Movent-se al xou")

    def quisoc(self):
        print("Som un xou")

# EXERCICI 73.5
# Llista d’objectes i bucle que crida els mateixos mètodes

elements = [
    Cavall(5),
    Dofi(3),
    Abella(1),
    Huma("Joan", 30),
    Fiet("Pere", 10, ["Joan", "Maria"]),
    Centaure("Quiró", 40),
    Xou()
]

for e in elements:
    e.quisoc()
    e.xerrar()
    e.mourem()

    if isinstance(e, Abella):
        e.picar()

    if isinstance(e, Fiet):
        e.nompares()

    print()
