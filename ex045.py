from random import randint
from time import sleep
print("=== PEDRA, PAPEL OU TESOURA ===")
esc = (str(input("Você escolhe o que: "))).upper().strip()
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!!")

cpu = int(randint(0, 2))
if cpu == 0:
    cpu = "PEDRA"
elif cpu == 1:
    cpu = "PAPEL"
else:
    cpu = "TESOURA"

if (esc == "PAPEL") and (cpu == "PAPEL"):
    print("-=" * 8)
    print("Você: {}".format(esc))
    print("CPU: {}".format(cpu))
    print("-=" * 8)
    print("\033[1;34mANULADO\033[m")
    print("-=" * 8)
elif (esc == "PAPEL") and (cpu == "PEDRA"):
    print("-=" * 8)
    print("Você: {}".format(esc))
    print("CPU: {}".format(cpu))
    print("-=" * 8)
    print("\033[1;32mVOCÊ GANHOU!!\033[m")
    print("-=" * 8)
elif (esc == "PAPEL") and (cpu == "TESOURA"):
    print("-=" * 8)
    print("Você: {}".format(esc))
    print("CPU: {}".format(cpu))
    print("-=" * 8)
    print("\033[1;31mVOCÊ PERDEU...\033[m")
    print("-=" * 8)
elif (esc == "PEDRA") and (cpu == "PEDRA"):
    print("-=" * 8)
    print("Você: {}".format(esc))
    print("CPU: {}".format(cpu))
    print("-=" * 8)
    print("\033[1;34mANULADO\033[m")
    print("-=" * 8)
elif (esc == "PEDRA") and (cpu == "PAPEL"):
    print("-=" * 8)
    print("Você: {}".format(esc))
    print("CPU: {}".format(cpu))
    print("-=" * 8)
    print("\033[1;31mVOCÊ PERDEU...\033[m")
    print("-=" * 8)
elif(esc == "PEDRA") and (cpu == "TESOURA"):
    print("-=" * 8)
    print("Você: {}".format(esc))
    print("CPU: {}".format(cpu))
    print("-=" * 8)
    print("\033[1;32mVOCÊ GANHOU!!\033[m")
    print("-=" * 8)
elif (esc == "TESOURA") and (cpu == "TESOURA"):
    print("-=" * 8)
    print("Você: {}".format(esc))
    print("CPU: {}".format(cpu))
    print("-=" * 8)
    print("\033[1;34mANULADO\033[m")
    print("-=" * 8)
elif (esc == "TESOURA") and (cpu == "PAPEL"):
    print("-=" * 8)
    print("Você: {}".format(esc))
    print("CPU: {}".format(cpu))
    print("-=" * 8)
    print("\033[1;32mVOCÊ GANHOU!!\033[m")
    print("-=" * 8)
elif (esc == "TESOURA") and (cpu == "PEDRA"):
    print("-=" * 8)
    print("Você: {}".format(esc))
    print("CPU: {}".format(cpu))
    print("-=" * 8)
    print("\033[1;31mVOCÊ PERDEU...\033[m")
    print("-=" * 8)
else:
    print("\n" * 160)
    print("-=" * 8)
    print("\033[1;31mERRO!\033[m")
    print("Você só pode escolher entre PEDRA, PAPEL ou TESOURA")
    print("Tente novamente!")
    print("-=" * 8)
