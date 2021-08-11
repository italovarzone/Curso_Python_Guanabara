n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
print("==== Calculando.... ====")

if n1 > n2 and n1 > n3:
    print("O primeiro numero digitado é o maior!")
    print("Primeiro número digitado foi: {}".format(n1))
elif n2 > n1 and n2 > n3:
    print("O segundo número digtado é o maior!")
    print("Segundo número digitado foi: {}".format(n2))
else:
    print("O terceiro número digtado é o maior!")
    print("Terceiro número digitado foi: {}".format(n3))
print("==== FIM ====")
