sanduiches_especiais ={
    "especial_1":"mega stacker rodeio 2.0",
    "especial_2":"mega stacker rodeio 3.0",
    "especial_3":"Whopper rodeio",
    "especial_4":"Whopper barbecue bacon",
    "especial_5":"Whopper duplo",
    "especial_6":"Whopper furioso",
    "especial_7":"mega stacker cheddar 2.0",
    "especial_8":"mega stacker cheddar 3.0",
    "especial_9":"mega stacker 2.0",
    "especial_10":"mega stacker 3.0"
}

sanduiches_carne={
    "carne_1":"Whopper",
    "carne_2":"Chedar Duplo",
    "carne_3":"Stacker Duplo bacon",
    "carne_4":"Rodeio duplo",
    "carne_5":"Big king",
    "carne_6":"Chesseburguer duplo",
    "carne_7":"Chesseburguer",
    "carne_8":"Rodeio",
    "carne_9":"Whopper JR"
}

sanduiches_frango={
    "frango_1":"Chicken Júnior",
    "frango_2":"Chiken Duplo",
    "frango_3":"BK Chicken Crispy",
    "frango_4":"Whopper Vegetariano"
}

prefixo_especial = "especial_"
prefixo_carne = "carne_"
prefixo_frango = "frango_"
sufixo = 1
escolha =int(input("Escolha o tipo de sanduíche: \n 1 - Especial \n 2 - Carne \n 3 - Frango \n Escolha:"))
if escolha == 1:
    while sufixo<11:
        print(f' {str(sufixo)} - {sanduiches_especiais[prefixo_especial+str(sufixo)]}')
        sufixo+=1
    sufixo = int(input("Escolha seu sunduíche pelo número: "))
    print(f'{sanduiches_especiais[prefixo_especial+str(sufixo)]}')

if escolha == 2:
    while sufixo<10:
        print(f' {str(sufixo)} - {sanduiches_carne[prefixo_carne+str(sufixo)]}')
        sufixo+=1
    sufixo = int(input("Escolha seu sunduíche pelo número: "))
    print(f'{sanduiches_carne[prefixo_carne+str(sufixo)]}')

if escolha == 3:
    while sufixo<5:
        print(f' {str(sufixo)} - {sanduiches_frango[prefixo_frango+str(sufixo)]}')
        sufixo+=1
    sufixo = int(input("Escolha seu sunduíche pelo número: "))
    print(f'{sanduiches_frango[prefixo_frango+str(sufixo)]}')

