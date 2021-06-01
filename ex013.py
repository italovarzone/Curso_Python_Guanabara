nome = input('Digite seu nome: ')
salar = float(input('Digite seu salário atual: '))

aum = salar * 15/100
salarfinal = salar + aum
print('{}, com 15% de aumento, seu salário agora é igual a: R${:.2f}'.format(nome, salarfinal))
