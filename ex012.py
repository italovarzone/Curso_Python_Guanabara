preco = float(input('Digite o preço do produto: '))
desc = preco * 5/100
precofinal = preco - desc
print('Com 5% de desconto, o produto ficou no valor de: R${:.2f}'.format(precofinal))