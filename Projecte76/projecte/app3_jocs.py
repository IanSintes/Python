# app3_jocs.py
import random

def jugar():
    print("\n--- APLICACIÓ 3: Joc - Endevina el número ---")
    numero = random.randint(1, 50)

    intents = 0

    while True:
        intents += 1
        guess = int(input("Endevina un número del 1 al 50: "))

        if guess == numero:
            print(f"Correcte! Has encertat en {intents} intents.")
            break
        elif guess < numero:
            print("És més gran.")
        else:
            print("És més petit.")

