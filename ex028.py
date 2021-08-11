from random import randint
nsortido = randint(0, 5)

n = int(input("Digite o número que estou pensando (entre 0 e 5): "))
if n == nsortido:
    print("\033[1;32mVOCÊ VENCEU!!\033[m")
else:
    print("\033[1;31mVOCÊ PERDEU...\033[m")
    print("O numero foi: {}".format(nsortido))
print("==== FIM ====")