def paraules_que_comencen(llista, lletra):
    return list(filter(lambda p: p.startswith(lletra), llista))

# Proves
paraules = ["maria", "manta", "peu", "mà"]
print(paraules_que_comencen(paraules, "p"))
print(paraules_que_comencen(paraules, "m"))