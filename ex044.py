valor = float(input("Valor do produto: "))
print("==== Formas de Pagamento ====")
print("[1] A vista em DINHEIRO/CHEQUE")
print("[2] A vista no CARTÃO")
print("[3] 2x no CARTÃO")
print("[4] 3x ou mais no CARTÃO")
print("=============================")
esc = int(input("Escolha: "))

if esc == 1:
    print("\n" * 160)
    desc = (valor * 10) / 100
    print("-=" * 16)
    print("Valor final: R${:.2f}".format(valor - desc))
    print("-=" * 16)
elif esc == 2:
    print("\n" * 160)
    desc = (valor * 5) / 100
    print("-=" * 16)
    print("Valor final: R${:.2f}".format(valor - desc))
    print("-=" * 16)
elif esc == 3:
    print("\n" * 160)
    print("-=" * 16)
    print("Valor final (Por mês): R${:.2f}".format(valor / 2))
    print("-=" * 16)
elif esc == 4:
    print("\n" * 160)
    print("-=" * 16)
    vzs = int(input("Quantas vezes você gostaria de fazer: "))
    print("-=" * 16)
    print("\n" * 160)
    print("-=" * 16)
    print("Valor final (Por mês): R${:.2f}".format(valor / vzs ))
    print("-=" * 16)
else:
    print("\n" * 160)
    print("-=" * 16)
    print("\033[1;31mERRO!!")
    print("-=" * 16)


