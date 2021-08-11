import time
nome = str(input("Digite seu nome: ")).upper().strip()
salario = float(input("Digite seu salário: "))
print("Processando... ")
time.sleep(2)
print("Processando... ")
time.sleep(2)
print("Processando... ")
time.sleep(3)
print("\n" * 130)
print("===== PAINEL ====")
print(("Nome do funcionário: {}".format(nome)))
print("Salário: R${:.2f}".format(salario))
print("=================")
if salario > 1250.00:
    aumento = (salario * 10) / 100
    salariofinal = salario + aumento
    print("Funcionário, você teve um aumento de: R${:.2f}".format(aumento))
    print("Salário final: R${:.2f}".format(salariofinal))
elif salario <= 1250.00:
    aumento = (salario * 15) / 100
    salariofinal = salario + aumento
    print("Funcionário, você teve um aumento de: R${:.2f}".format(aumento))
    print("Salário final: R${:.2f}".format(salariofinal))
print("=====  FIM  =====")


