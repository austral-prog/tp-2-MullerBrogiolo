def change():
    expense = 23.75
    money = 100

 # Solicito los datos al usuario
    costo = float(input("Me sale "))
    pago = float(input("Le entregué "))

# Calculo el vuelto total
    vuelto = pago - costo

# Separo en pesos y centavos
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

# Imprimo la respuesta:
    print("Me deben dar de vuelto:")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
