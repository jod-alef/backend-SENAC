resposta = ""

while resposta != "sair":
    mensagem = input("Digite uma mensagem: ")
    print("Mensagem recebida com o seguinte conteúdo:")
    print(mensagem)
    resposta = input("Você gostaria de continuar ou sair?").lower()

