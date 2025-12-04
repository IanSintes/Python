def lenp(frase):
    paraules = frase.split()
    return list(map(len, paraules))

frase = "Soc del Ramis i m'agrada programar"
print(lenp(frase))
