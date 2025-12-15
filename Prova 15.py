import json

# Obrim el fitxer json i carreguem la informacio dins un diccionari 
with open("ex2.json","r") as f:
    dades=json.load(f) 
    print(dades)
    
# Obrim el fitxer json per escriure i modifiquem el diccionari  i ho guardem tot dins el fitxer que elimina el que hi havia abans.
with open("ex2.json","w") as f:
    dades["colors"]=["blanc","negre","verd","groc"]
    json.dump(dades,f)




"""

with open("ex2.json","r") as f:
    dades=json.load(f)

l= list(dades["colors"])
print(l)



for x,y in dades.items():
    print("Clau: {} i valor {}".format(x,y))

for x in dades:
    print(x)


dadesjson = '{"nom":"Joan","edad":45}'
dades = json.loads(dadesjson)
print(dades)
for x,y in dades.items():
    print("Clau:{} i valor {}".format(x,y))
"""