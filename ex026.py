frase = str(input("Digite uma frase: ")).strip().upper()
print("Possuí na frase a letra 'A' {} vezes".format(frase.count("A")))
print("A letra 'A' apareceu a primeira vez na posição {}".format(frase.find("A")+1))
print("A letra 'A' foi encontrada a ultima vez na posição {}".format(frase.rfind("A")+1))


