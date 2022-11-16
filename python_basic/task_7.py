"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class Complex:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def a(self):
        return self.a

    def b(self):
        return self.b

    def __add__(self, other):
        if not isinstance(other, Complex):
             raise TypeError("Второй операнд не является экземпляром класса Complex")
        return Complex(self.a + other.b, self.a + other.b)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            raise TypeError("Второй операнд не является экземпляром класса Complex")
        a_val = self.a * other.a - self.b * other.b
        b_val = self.a * other.b + other.a * self.b
        return Complex(a_val, b_val)

    def __str__(self):
        return f"{self.a} + {self.b} * i"


n1 = Complex(1, 4)
n2 = Complex(3, -2)
n3 = n1 + n2
print(f"n1 + n2 = {n3}")
n4 = n1 * n2
print(f"n1 * n2 = {n4}")
