def ada():
    first_name = "AdA"
    last_name = "LoVeLAce"
    
    # a) Pasar el nombre completo a minúsculas:
    full_name_lower = first_name.lower() + " " + last_name.lower()
    print(full_name_lower)  # ada lovelace
    
    # b) Pasar la primer letra de cada palabra a mayúscula:
    first_letter_mayus = first_name.capitalize() + " " + last_name.capitalize()
    print(first_letter_mayus)  # Ada Lovelace
    
    # c) Colocar todas las letras en mayúsculas:
    full_name_upper = first_name.upper() + " " + last_name.upper()
    print(full_name_upper)  # ADA LOVELACE
    
    # d) Generar un espacio antes de escribir todas las letras en minúsculas:
    spaced_full_name_lower = "\t" + first_name.lower() + " " + last_name.lower()
    print(spaced_full_name_lower)  #     ada lovelace
