# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141
from math import pi

d =  int(input("Введите число для заданной точности числа Пи:\n"))
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')