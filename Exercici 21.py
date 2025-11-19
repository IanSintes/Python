def es_palindrom(paraula):
    paraula = paraula.lower()
    return paraula == paraula[::-1]

# Exemples de prova
print("es_palindrom('radar') =", es_palindrom('radar'))
print("es_palindrom('ara') =", es_palindrom('ara'))
print("es_palindrom('civic') =", es_palindrom('civic'))
print("es_palindrom('Python') =", es_palindrom('Python'))
print("es_palindrom('Rallar') =", es_palindrom('Rallar'))