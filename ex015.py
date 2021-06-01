tot_dias = int(input('Quantos dias você ficou com o carro: '))
km_rodado = int(input('Digite quantos quilometros (km) foram rodados: '))

tot_gasto = (tot_dias * 60) + (km_rodado * 0.15)
print('O total gasto foi R${:.2f}'.format(tot_gasto))
