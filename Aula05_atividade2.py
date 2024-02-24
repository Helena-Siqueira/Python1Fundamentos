import random

numero_sorteado = random.randint(0, 100)
numero_escolhido = 0  

print("Adivinhe um número de 0 a 100:")

while numero_escolhido != numero_sorteado:

    numero_escolhido = int(input())

    if(numero_escolhido < numero_sorteado):
        print("O número é MAIOR, tente de novo")
        erros +=1
    if(numero_escolhido > numero_sorteado):    
        print("O número é MENOR, tente de novo")
        erros +=1
    if(numero_escolhido == numero_sorteado):  
        print("Parabéns você acerto")
        print(f"Você errou {erros} vezes")    

    
              
