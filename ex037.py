inteiro = int(input("Digite um número inteiro: "))
print("""Escolha uma das  opções:
=======================================
[1] Converter o número para BINÁRIO
[2] Converter o número para OCTAL
[3] Converter o número para HEXADECIMAL
=======================================""")
esc = int(input("Sua escolha: "))

if esc == 1:
    print("=" * 39)
    print("O número {} convertido em BINÁRIO é {}".format(inteiro, bin(inteiro)[2:]))
elif esc == 2:
    print("=" * 39)
    print("O número {} convertido em OCTAL é {}".format(inteiro, oct(inteiro)[2:]))
elif esc == 3:
    print("=" * 39)
    print("O número {} convertido em HEXADECIMAL é {}".format(inteiro, hex(inteiro)[2:]))
else:
    print("=" * 39)
    print("Erro!")
    print("Escolha inválida, tente novamente!")