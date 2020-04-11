# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

get_prime_numbers(1000)


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.prime_numbers = []
        self.n = n
        self.i = 0

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        self.i += 1
        for number in range(self.i, self.n + 1):
            for prime in self.prime_numbers:
                if number % prime == 0:
                    break
            else:
                self.prime_numbers.append(number)
                self.i = number
                return number

        raise StopIteration()



prime_number_iterator = PrimeNumbers(n=1000)
for number in prime_number_iterator:
    print(number)

# зачет!
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            yield number
            prime_numbers.append(number)




for number in prime_numbers_generator(n=10000):
    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True


def function1(number):
    number = [int(i) for i in str(number)]
    res = len(number) // 2
    return sum(number[:res]) == sum(number[-res:])


for item in filter(function1, prime_numbers_generator(1000)): print(item)

# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101

def function2(number):
    number = str(number)
    res = len(number) // 2
    return number[:res] == number[::-1][:res]


for item in filter(function2, prime_numbers_generator(1000)): print(item)

# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
# Циклическое число:
# 142857 × 2 = 285714

def function3(number):
    number = str(number)
    return int(number)*2 == int(number[2:]+number[:2])


for item in filter(function3, prime_numbers_generator(1000)): print(item)

# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
# зачет!