f = str(input("Digite uma frase: ")).upper().strip()
separado = f.split()
junto = "".join(separado)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("\033[1;32mA frase é um PALÍNDROMO!")
else:
    print("\033[1;31mA frase NÃO é um PALÍNDROMO!")
