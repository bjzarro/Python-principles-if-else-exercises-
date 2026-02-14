# Fazer um sistema de login, com usuário e senha pré-definidos

usuario = str(input("Digite seu nome de usuário:"))
senha = str(input("Digite sua senha:"))

if usuario == ("matheus") and senha == ("bizarro"):
    print("Você foi logado com sucesso.")
    
    print("Escolha uma opção:")
    print("1 - Ler uma frase motivacional")
    print("2 - Ler uma frase desmotivacional")
    print("3 - Conferir login e senha")
    print("4 - Sair")
    
    escolha = input(":")
    if escolha == ("1"):
        print("Vai dar tudo certo, confia.")
    
    elif escolha == ("2"):
        print("Nem tenta, que vai dar errado.")
    
    elif escolha == ("3"):
        print("O usuário é 'matheus' e a senha é 'bizarro'")
    
    elif escolha == ("4"):
        print("FIM.")
    
    else:
        print("Opção incorreta, não dê espaço.")


else:
    print("Usuario ou senha incorretos.")
    