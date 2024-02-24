# Operções aritméticas


# Adição
print(15+2)
print(20+5)
print("20"+str(5))

# Subtrção 
print(2-10)
print(0.85-2)

# Multiplicação
print(4*2)

# Divisão
print(2/3)

# Contas grandes
print(2+2+5-3*5/0.5*1.8+5.5-8*-1+100)

print("________________________________________________________")
# Operações com variáveis
soma = 5+5
print(soma)


numero = 80
numero2 = 9
conta = numero + numero2
print(conta)

aluguel = 700
condomínio = 200
total = aluguel + condomínio
print(total)
iptu = 150.85
total_contas = total + iptu
print(total_contas)


print("________________________________________________________")

# Incremento de variável
moedas = 0


# O personagem pegou UMA moeda
moedas = moedas + 1
# O personagem pegou mais UMA moeda
moedas = moedas + 1
# O personagem ganhou 3 moedas
moedas = moedas + 3
# O personagem pegou mais UMA moeda
moedas += 1
# O personagem ganhou 158 moedas
moedas += 158


# O personagem perdeu 5 moedas
moedas -=5
# Multiplicou em 2 as moedas
moedas *=2
# O personagem pegou 1580 moedas
moedas +=1580
# O personagem perdeu metade das moedas
moedas /=2
# O personagem ganhou 50% das moedas atuais
moedas = moedas + (moedas /2)
# ou: moedas = moedas * 1.5
# ou: moedas = moedas * 0.5 + moedas 

print(f"{moedas} Moedas")



print("________________________________________________________")

# Calculo de porcentagem
preco_camiseta = 65.90
desconto_a_vista = 0.10
valor_desconto = preco_camiseta * desconto_a_vista
valor_final = preco_camiseta - valor_desconto
print(f"O desconto de {desconto_a_vista*100}% é de R$ {round(valor_desconto,2)} e o valor final do produto é de R$ {valor_final}")
# Comando round(valor,casas) para arrendondar






















