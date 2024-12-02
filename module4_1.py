from fake_math import divide as fake_m
from true_math import divide as true_m

a = int(input("Введите делитель: "))
b = int(input("Введите делимое: "))
print('Школьная математика:', fake_m(a, b))
print('Высшая математика:', true_m(a, b))