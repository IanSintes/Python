while True:
    capital = float(input("Introdueix el capital (50000 - 800000 €): "))
    if 50000 <= capital <= 800000:
        break
    print("Capital fora de rang.")

while True:
    interes = float(input("Introdueix l'interès (0.5% - 13%): "))
    if 0.5 <= interes <= 13:
        break
    print("Interès fora de rang.")

while True:
    anys = int(input("Introdueix els anys (3 - 40): "))
    if 3 <= anys <= 40:
        break
    print("Anys fora de rang.")

capital_final = capital * (1 + interes / 100) ** anys

print("Capital final:", round(capital_final, 2), "€")
