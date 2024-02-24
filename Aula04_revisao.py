#Revisão aula 03

print("Digite o seu nome:")
nome = input()
nome = nome.capitalize()
# valor condição valor
if nome == "":
    print("Você não digitou um nome válido")
if len(nome) < 3:
    print("O nome digitado é muito curto")

print("Digite o seu sobrenome:")
sobrenome = input()
sobrenome.capitalize()

if sobrenome =="":
    print("Você não digitou um sobrenome...")
if len(sobrenome) < 3:
    print("O sobrenome digitado é muito curto...")


print("Olá, bom dia, ",nome," ",sobrenome)      
nome_completo = nome.capitalize() + "" + sobrenome.capitalize()      
print(f"Olá bom dia, {nome}  {sobrenome}")



