n = int(input("Digite um número: "))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        total += 1
        print("\033[1;31m", end='')
    else:
        print("\033[1;33m", end='')
    print("{} ".format(c), end='')
print("\n\033[mO número {} foi dividido {} vezes.".format(n, total))
if total == 2:
    print("\033[1;32mEsse número é PRIMO")
else:
    print("\033[1;31mEsse número NÃO é PRIMO")
