def primos(x):
    for i in range(2,x):
        j=2
        contador = 0
        while j < i:
            if i % j == 0:
                contador = 1
                j = j+1
            else:
                j = j+1
        if contador == 0:
            print(str(i) + " é um número primo")
            contador = 0
        else:
            contador = 0

nPrimos = int(input("Digite o número para verificar os primos na sequencia"))
primos(nPrimos)