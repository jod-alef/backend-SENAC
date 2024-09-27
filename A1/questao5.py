nota = float(input("Digite a nota do aluno:"))
if nota < 3:
    print("Insuficiente")
elif nota < 5:
    print("Satisfatório")
elif nota < 8:
    print("Bom")
else:
    print("EXCELENTE!")