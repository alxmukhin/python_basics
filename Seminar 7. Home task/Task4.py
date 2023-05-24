"""Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки второй
матрицы и т.д.
"""


class Matrix:
    def __init__(self, first_matrix):
        self.first_matrix = first_matrix

    def __str__(self):
        return "\n".join(["\t".join([str(i) for i in row]) for row in
                          self.first_matrix])

    def __add__(self, second_matrix):
        new_matrix = []
        for i in range(len(self.first_matrix)):
            row = []
            for j in range(len(self.first_matrix[0])):
                row.append(self.first_matrix[i][j] +
                           second_matrix.first_matrix[i][j])
            new_matrix.append(row)
        return Matrix(new_matrix)


matrix1 = Matrix([[2, 3], [21, 8], [10, 1]])
print(matrix1)
print()
matrix2 = Matrix([[3, 7], [3, 28], [17, 4]])
print(matrix2)
print()

matrix3 = matrix1 + matrix2
print(matrix3)
