import math
print("введите значение для расчёта функции")
x=float(input("Введите знчение x:"))
y=float(input("Введите знчение y:"))
U= (((8+ abs(x-y)**2 + 1)**(1/3))/(x**2 + y**2 +2)) - math.e**abs(x-y)
print("Значение функции =", float(U))