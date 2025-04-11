def change():
    expense = 23.75
    money = 100
    
# Solicitar los datos de entrada al usuario
    print("**Ingresar gasto:**")
    gasto = float(input())  # Convertimos a float para manejar decimales
    print("**Dinero recibido**")
    dinero_recibido = float(input())

# Calcular el vuelto total
    vuelto = dinero_recibido - gasto

# Separar pesos y centavos
    pesos = int(vuelto)  # Obtenemos la parte entera
    centavos = round((vuelto - pesos) * 100)  # Obtenemos los centavos redondeados

# Mostrar el informe con el formato exacto requerido
    print("\n**Vuelto**\n")  # \n para saltos de línea
    print("**Pesos:**")
    print(pesos)
    print("\n**Centavos:**")
    print(centavos)
