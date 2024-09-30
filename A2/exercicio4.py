# Simulador de Dados Financeiros
# Objetivo: Simular o saldo de uma conta com juros compostos usando loops e incrementadores.
# - Descrição: Solicite ao usuário um saldo inicial, a taxa de juros anual e o número de anos. Use um loop ‘while’ para
# simular o aumento do saldo com juros compostos ao longo dos anos e imprima o saldo final após o período especificado.

capital = float(input("Digite o saldo inicial da conta:"))
jurosAno = float(input("Digite a porcentagem da taxa de juros anual: "))/100
anos = int(input("Digite o numero de anos: "))
anoAtual = 0
capitalInicial = capital

while anoAtual != anos:
    for n in range(anos):
        anoAtual += 1
        capital = capital * (1 + jurosAno)
        print(f"Seu saldo após o {anoAtual}º ano é de R$ {capital:.2f}")
    else:
        print(f"Você lucrou R$ {(capital - capitalInicial):.2f} no periodo de {anos} anos")




