print("Digita sua 1ª nota:")
nota1 = float(input() )
print("Digite sua 2ª nota:")
nota2 = float(input() )

media = (nota1 + nota2) / 2 
print("Sua média é", media)

if media >= 7:
    print("Parabéns, você está APROVADO!")
else: 
    print(f"Sua média é menor que 7, infelizmente você foi reprovado; tchuru.")
