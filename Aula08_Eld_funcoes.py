def exibe_cabecalho(titulo, separador):
    print(separador*30)
    print(f"{titulo} ")
    print(separador*30)
    print()
    print()

def calcula_area_retangulo(base, altura):
    area = base * altura
    # print(area)
    return area


exibe_cabecalho("Meu programa", "=")
# exibe_cabecalho("Cadastro de usuario", "*")
total = calcula_area_retangulo(11,37) + calcula_area_retangulo(23,57)
#print(calcula_area_retangulo(11, 37))
print(total)