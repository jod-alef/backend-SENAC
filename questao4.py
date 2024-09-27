idade = int(input("Qual a sua idade?"))

if idade < 10:
    print("Criança")
elif idade < 13:
    print("Pré-Adolescente")
elif idade < 19:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")