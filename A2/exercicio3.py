numero = input("Entre um número decimal positivo com mais de 4 casas decimais: ")
numero = float(numero.replace(',', '.'))

print(f"Seu número sem formatação é mostrado no python assim: {numero}")
print(f"Após formatação, seu número fica assim: {numero:.2f}")