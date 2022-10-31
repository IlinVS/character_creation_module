from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculatesquareroot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Функция проводит арифметические вычисления."""
    if your_number <= 0:
        return
    print(
        'Мы вычислили квадратный корень из введённого вами числа. '
        'Это будет: {calculatesquareroot(your_number)}')


print(message)
calc(25.5)

from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Функция проводит арифметические вычисления."""
    numb = calculate_square_root(your_number)
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень '
          f'из введённого вами числа. Это будет:'
          f'{numb}')


print(message)
calc(25.5)
