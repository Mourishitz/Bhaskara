#Inputs para os valores a, b, c da fórmula
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))

# variavel da fórmula de delta dentro de Bhaskara (B²-4ac)
delta = (b ** 2) - 4 * a * c
# algoritmo para detectar se delta é igual ou menor que 0, pois se delta for de fato menor que zero será uma raíz não real
if a == 0:
    print("a != 0")
elif delta < 0:
    print("Sem raízes reais")
# resto do calculo com base nos resultados de delta
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print("x1:{}, x2:{}".format(x1, x2))
