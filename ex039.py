print("Qual sua idade, cidadão?")
age = int(input("Idade: "))
enlistment = 18 - age

if enlistment == 0:
    print("Esse ano você se apresenta ao Tiro de Guerra de sua cidade!")
elif enlistment > 0:
    if enlistment == 1:
        print("Você se alistará em {} ano! Fique Atento!".format(enlistment))
    else:
        print("Fique tranquilo!")
        print("Você se alistará em {} anos!".format(enlistment))
else:
    exced = enlistment * -1
    if exced == 1:
        print("Já excedeu {} ano do seu alistamento!".format(exced))
    else:
        print("Já excedeu {} anos do seu alistamento!".format(exced))
