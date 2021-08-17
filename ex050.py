s = 0
for c in range(1, 7):
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        s += n
print("\n" * 1)
print("A soma dos números pares é: {}".format(s))
