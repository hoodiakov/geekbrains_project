"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

class Date:
    def __init__(self, date: str):
        self.date = date
        try:
            self.day, self.month, self.year = Date.date_digit(self.date)
            Date.validation(self.day, self.month, self.year)
        except TypeError:
            pass

    @classmethod
    def date_digit(cls, date_str: str):
        try:
            day, month, year = map(int, date_str.split('-'))
            return day, month, year
        except ValueError:
            print('Введенные данные не числа даты')

    @staticmethod
    def validation(day: int, month: int, year: int):
        itm = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if day in range(1, itm[month] + 1) and 1 <= month < 13 and 1 <= year < 2021:
            pass
        else:
            raise ValueError(f'Данные {day}-{month}-{year} не соответствуют календарю')

    def __str__(self):
        try:
            return f"Число {self.day} месяц {self.month} год {self.year}"
        except AttributeError:
            return f'Ошибка в строке {self.date}'


dat = Date('ad-06-2007')
dat2 = Date('31-08-2020')
dat3 = Date('9-02-20')
print(dat)
print(dat2)
print(dat3)
