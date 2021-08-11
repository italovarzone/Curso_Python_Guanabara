KmsViagem = float(input("Digite quantos Km terá sua viagem: "))
if KmsViagem <= 200:
    preco = KmsViagem * 0.50
    print("Sua passagem custara em torno de R${:.2f}".format(preco))
    print("Boa viagem, cidadão!")
else:
    preco = KmsViagem * 0.45
    print("Sua passagem custará em torno de R${:.2f}".format(preco))
    print("Boa viagem, cidadão!")

