def change():
    expense = 23.75
    money = 100

# Calculo el vuelto
    vuelto = money - expense

# Separar pesos y centavos
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

# Imprimir el informe respetando el formato}
    print("Vuelto")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
