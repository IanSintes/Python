paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

p1 = paraula1.lower()
p2 = paraula2.lower()

if len(p1) >= 3 and len(p2) >= 3 and p1[-3:] == p2[-3:]:
    print("Rimen")
elif len(p1) >= 2 and len(p2) >= 2 and p1[-2:] == p2[-2:]:
    print("Rimen un poc")
else:
    print("No rimen")
