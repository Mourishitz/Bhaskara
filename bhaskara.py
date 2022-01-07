a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
delta = (b ** 2) - 4 * a * c
if a == 0:
    print("a != 0")
elif delta < 0:
    print("Sem raízes reais")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print("x1:{}, x2:{}".format(x1, x2))