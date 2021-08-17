maiorpeso = 0
menorpeso = 0
for c in range(0+1, 6):
    peso = float(input("Digite o {}º peso: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(maiorpeso)
print(menorpeso)


