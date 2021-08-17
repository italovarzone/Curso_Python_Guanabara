n = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a RAZÃO agora: "))
decimo = n + (10 - 1) * r
for c in range(n, decimo + r, r):
    print("{} ".format(c), end='-> ')
print("FIM...")