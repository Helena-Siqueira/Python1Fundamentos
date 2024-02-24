# Estrutura de programas em Python

def main():
    
    print("Digite seu usuário")
    usuário = input()

    # Verificar se o usuário é válido
    if len(usuário) < 3:
        print("O usuário está incorreto...")
        return # Encerra o sistema
    print("Digite sua senha:")
    senha = input()
    if len(senha) < 3:
        print("A senha está incorreta")
        return        
    print("Login efetuado com sucesso!")

    print("Você gostaria de reiniciar o sistema")
    resposta = input()

    if resposta.lower() == "sim":
        main()
    else: 
        print("Ok, tenha um bom dia")        
    
    

main() 