velCarro = float(input("Digite a velocidade que seu carro passou: "))
if velCarro > 80:
    multa = (velCarro - 80) * 7.00
    print("Cidadão, seu veículo passou da velocidade permitida do radar!")
    print("==> Será aplicado uma multa de |R${:.2f}| em seu nome.".format(multa))
else:
    print("Boa viagem cidadão, não ande mais de 80km nessa pista!")
    print("==> Não foi aplicado nenhuma multa.")