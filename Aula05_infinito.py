# LOOPS (quase) infinitos

repetir = (True)

while repetir == True:

    print("Olá, deseja repetir? Digite SIM ou NÃO:")
    resposta = input()

    if resposta == "SIM":
        repetir = True
    else:
        repetir = False    

# Abaixo, outra forma de resolver.
# if resposta == "NÃO":        
#    repetir = False