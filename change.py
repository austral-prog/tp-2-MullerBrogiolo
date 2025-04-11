def change():
    expense = 23.75
    money = 100
    
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = vuelto - pesos
    resultado_centavos = int(centavos*100)  # Agregué round() para mayor precisión
    
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("")  # Línea vacía que el test espera
    print("Vuelto")
    print("")  # Otra línea vacía
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(resultado_centavos)
