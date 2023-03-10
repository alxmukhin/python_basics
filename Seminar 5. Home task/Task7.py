"""Задание 7.

Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def progression(n, result=0, i=0):
    if i > n:
        print(f"Результат вычисления 1 + 2 + ... + {n} с помощью рекурсии:"
              f" {result}")
        return
    else:
        result = result + i
        i += 1
    progression(n, result, i)


number_of_elements = int(input("Введите натуральное число n: "))
progression(number_of_elements)
print("Результат вычисления с помощью формулы n(n+1)/2:"
      f" {int(number_of_elements * (number_of_elements + 1) / 2)}")
