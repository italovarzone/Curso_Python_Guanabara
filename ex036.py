#INTERAÇÃO COM O USUÁRIO E CAPTURANDO
#AS ENTRADAS DE DADOS:

print("-=-" * 10)
print("       BANCO DO BRASIL")
print("-=-" * 10)
print("Olá, qual seu nome? ")
name = str(input("Nome: "))
print("{}, qual o valor da casa? ".format(name))
house_value = float(input("Valor: R$"))
print("Agora, diga qual seu salário")
salary = float(input("Salário: R$"))
print("Em quantos anos você pretende pagar a casa? ")
years = int(input("Anos a pagar: "))

#CALCULOS:
installments = house_value / years
exceeded = (salary * 30) / 100
mounth = installments / 12

#ESTRUTURA DE CONDIÇÕES:
if exceeded > mounth:
    print("\n" * 160)
    print("-=-" * 10)
    print("\033[32mParabéns\033[m, você efetuou o empréstimo com sucesso!")
    print("Você pagará parcelas de R${:.2f} por mês!".format(mounth))
    print("Te esperamos em breve, {}!".format(name))
    print("-=-" * 10)
else:
    print("\n" * 160)
    print("-=-" * 10)
    print("\033[31mEmpréstimo negado!\033[m")
    print("Infelizmente seu salário não permite efetuar o empréstimo.")
    print("-=-" * 10)






