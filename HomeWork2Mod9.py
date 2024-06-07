"""Функция возвращает умножение и сложение"""
print("Задача 1. Фабрика функций")
def math_func(oper):
    if oper == "multi":
        def multi(x, y):
            return x * y
        return multi

    if oper == "add":
        def add(x, y):
            return x + y
        return add

my_func = math_func("multi")
print(my_func(10, 20))
my_func = math_func("add")
print(my_func(5, 15))

"""Лямбда-функция и ее аналог через def"""
print("Задача 2. Лямбда-функции")
deg_num4 = lambda x: x ** 4
print(deg_num4(4))

def deg_num4_def(x):
   return x ** 4
print(deg_num4_def(4))

"""Вызываемые объекты"""
print("Задача 3. Вызываемые объекты")

class Rect:
    def __init__(self, a):
        self.a = a
    def __call__(self, b):
        return self.a * b

print("Стороны 30, 40")
my_sq = Rect(30)
print(f"Площадь {my_sq(40)}")
