a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

delta = b ** 2 - 4 * a * c
if a == 0:
    print("A tem que ser diferente de zero.")
elif delta < 0:
    print("Não possui raízes reais.")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))
