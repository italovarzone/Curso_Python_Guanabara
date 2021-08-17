totalmenor = 0
totalmaior = 0
for c in range(0+1, 8):
    idade = int(input("Digite a idade da {}ª pessoa: ".format(c)))
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print("Total de MAIORES de idade: {}".format(totalmaior))
print("Total de MENORES de idade: {}".format(totalmenor))

