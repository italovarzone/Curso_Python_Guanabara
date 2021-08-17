somaidades = 0
maioridade = 0
totalmulher20 = 0
nomevelho = ''
for c in range(1, 5):
    print("===== {}ª Pessoa =====".format(c))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidades += idade
    if c == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
media = somaidades / 4
print("")
print("A média entre as idades é: {:.1f}".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(maioridade, nomevelho))
print("O total de mulheres abaixo de 20 anos é: {}".format(totalmulher20))




