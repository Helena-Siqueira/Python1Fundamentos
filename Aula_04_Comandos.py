# COMANDOS em Python para variável STRING

nome = "Helena Siqueira"

maiusculo = nome.upper()
minusculo = nome.lower()
quantidade = len(nome) # Qntde de caracteres
novo_nome = nome.replace("a", "@")

print( maiusculo )
print( minusculo )
print( nome )
print(nome.capitalize()) # Primeira letra maiúscula
print(quantidade)
print(novo_nome)

print("Não, não é possível não gostar de café.")
frase = "Não, não é possível não gostar de café."

frase_nova = frase.replace("não", "sim")
frase_nova = frase_nova.replace("Não", "Sim")

frase_nova = frase.lower()
frase_nova = frase.replace("não","sim")
frase_nova = frase_nova.replace("Não","Sim")
frase_nova = frase_nova.capitalize()



