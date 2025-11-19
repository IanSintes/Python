def crear_punts(llista):
    for num in llista:
        espais = (max(llista) - num) // 2
        print(" " * espais + "." * num)

def dibuixar_triangle():
    # Piràmide
    teulada = [1, 3, 5, 7, 9]
    crear_punts(teulada)

dibuixar_triangle()
