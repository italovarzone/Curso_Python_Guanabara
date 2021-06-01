from math import hypot
co = float(input('Digite o C.O do triângulo: '))
ca = float(input('Digite agora, o C.A do triângulo: '))
hip = hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hip))

