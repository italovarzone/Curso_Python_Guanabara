import datetime

date = datetime.date.today()
year = int(date.strftime("%Y"))

nasc = int(input("Ano de nascimento: "))
idade = year - nasc
if idade < 0:
    print("\033[1;32mERRO!!")

if idade <= 9:
    print("Idade: {} anos.")
    print("CATEGORIA: MIRIM")
elif idade <= 14:
    print("Idade: {} anos.")
    print("CATEGORIA: INFANTIL")
elif idade <= 19:
    print("Idade: {} anos.")
    print("CATEGORIA: JUNIOR")
elif idade <= 20:
    print("Idade: {} anos.")
    print("CATEGORIA: SÊNIOR")
else:
    print("Idade: {} anos.")
    print("CATEGORIA: MASTER")




