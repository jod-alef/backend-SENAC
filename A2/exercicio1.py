#import math

def fatores(x):
    y = []
    for t in range(x):
        y.append(t+1)
        #print(y)

    resultado = 1
    for i in y:
        resultado = resultado * i
    return resultado

    #Toda essa função acima poderia ser substituida apenas pela linha abaixo.
    #print(math.factorial(x))

numero = int(input("Entre um número não negativo, diferente de 0:"))
if numero <= 0:
    print("Você entrou um número negativo ou 0, não permitindo assim a fatoração")
else:
    print(f"O fatorial de {numero} é {fatores(numero)}")

