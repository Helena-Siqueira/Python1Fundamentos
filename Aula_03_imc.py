print("Digite seu peso:")
peso = input()   # Texto (string)
peso = float(peso) # número
print("Digite sua altura:")
altura = float(input() )

imc = peso / (altura * altura)
print("Resultado", imc)

if imc <= 18.6:
    print("Você está ABAIXO do peso")
else: 
    if imc >= 25:
        print("Você está acima do peso")
    else: 
        print("Você está no peso IDEAL")    


