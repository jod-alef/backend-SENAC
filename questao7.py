idade = int(input("Qual a sua idade?"))
if idade >= 18:
    print("Você pode viajar sem permissão de seus pais")
else:
    permissao = input("Você tem permissão para dos pais? (sim/não)").lower()
    if permissao == "sim":
        print("Você está liberado para viajar")
    elif permissao == "não" or "nao":
        print("Você não pode viajar")
    else:
        print("Resposta incorreta")