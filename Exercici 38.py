import random

def generar_codi():
    return [random.randint(0, 9) for _ in range(4)]

def comparar_codis(codi_secret, intent):
    encerts_posicio = 0
    coincidencies = 0

    codi_secret_copia = codi_secret.copy()
    intent_copia = intent.copy()

    # Comptem els encerts a la posició correcta
    for i in range(4):
        if intent[i] == codi_secret[i]:
            encerts_posicio += 1
            codi_secret_copia[i] = intent_copia[i] = None  # Marquem com a comptats

    # Comptem coincidències sense importar posició
    for i in range(4):
        if intent_copia[i] is not None and intent_copia[i] in codi_secret_copia:
            coincidencies += 1
            codi_secret_copia[codi_secret_copia.index(intent_copia[i])] = None

    return encerts_posicio, coincidencies

# Programa principal
codi_secret = generar_codi()
print("Benvingut a MasterMind!")
print("Intenta endevinar el codi de 4 xifres (del 0 al 9)")

intents = 0
while True:
    intent_str = input("Introdueix el teu intent: ")
    
    if len(intent_str) != 4 or not intent_str.isdigit():
        print("Has d'introduir exactament 4 xifres del 0 al 9.")
        continue

    intent = [int(x) for x in intent_str]
    intents += 1

    encerts, coincidencies = comparar_codis(codi_secret, intent)
    if encerts == 4:
        print(f"Enhorabona! Has encertat el codi en {intents} intents!")
        break
    else:
        print(f"Encerts a la posició correcta: {encerts}, coincidències en altres posicions: {coincidencies}")