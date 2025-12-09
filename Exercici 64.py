def concatenar_amb_connector(llista1, llista2, connector):
    return [a + connector + b for a, b in zip(llista1, llista2)]

# Proves
llista1 = ["sub", "supra"]
llista2 = ["campió", "campiona"]

print(concatenar_amb_connector(llista1, llista2, "-"))