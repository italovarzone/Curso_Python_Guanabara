n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
m = (n1 + n2) / 2

if m < 5.0:
    print("\n" * 160)
    print("-=" * 6)
    print("\033[1;31mREPROVADO!\033[m")
    print("Nota final: {:.1f}".format(m))
    print("-=" * 6)
elif (m >= 5.0) and (m < 6.9):
    print("\n" * 160)
    print("-=" * 6)
    print("\033[1;34mRECUPERAÇÃO!\033[m")
    print("Nota final: {:.1f}".format(m))
    print("-=" * 6)
else:
    print("\n" * 160)
    print("-=" * 6)
    print("\033[1;32mAPROVADO!\033[m")
    print("Nota final: {:.1f}".format(m))
    print("-=" * 6)
