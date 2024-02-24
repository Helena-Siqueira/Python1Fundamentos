print("Digite a sua idade:")
idade = float( input() )

# > Maior     <  Menor 
# >+ Maior OU igual    <= Menor OU igual
if idade >= 18:
    print("Você já pode tirar a CNH")
else:
#if idade < 18:
    idade_faltante = 18 - idade
    print(f"Você não tem idade, volte daqui {18 - idade} anos")

print("Fim do sistema...")    