# Jogo de adivinhação de números
import random
    
numero_sorteado = random.randint(0, 10)
numero_escolhido = 0 
tentativas = 0

print("Adivinhe um número de 0 a 10:")

while numero_escolhido != numero_sorteado:
    numero_escolhido = int(input())
    if(numero_escolhido != numero_sorteado):
        print("Você errou! Tente de novo:")
        tentativas +=1
    else:
        print("Parabéns, você acertou!") 
        print(f"Você errou {tentativas} vezes")

