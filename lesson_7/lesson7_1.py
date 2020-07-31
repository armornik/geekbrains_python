class MyException(Exception):
    pass


class Matrix:
    def __init__(self, any_list):
        self.any_list = [any_list[x] for x in range(len(any_list))]

    def __str__(self):
        result = ''
        check = []
        try:
            for matrix in self.any_list:
                check.append(len(matrix))
                result += str(matrix) + '\n'
            if len(set(check)) > 1:
                raise MyException()
        except MyException:
            return 'Каждый ряд матрицы должен быть одинаковой длинныы'
        return result

    def __add__(self, other):
        result = []
        try:
            res1, separator_matrix1, separator_line = matrix_decomposition(self.any_list)
            res2, separator_matrix2, separator_line = matrix_decomposition(other.any_list)
            if separator_matrix1 != separator_matrix2:
                raise MyException
            for elem in range(len(res1)):
                result.append(res1[elem] + res2[elem])
            output = []
            for line in range(separator_matrix1):
                output.append(result[0:separator_line])
                del result[0:separator_line]
            return output
        except TypeError:
            return 'Все элементы матрицы должны быть заполнены числами'
        except MyException:
            return 'Длина каждой строки матрицы должна быть одинакова'


def matrix_decomposition(matrix):
    res = []
    check_elem = []
    separator_matrix = len(matrix)
    separator_line = len(matrix[0])
    for row in matrix:
        check_elem.append(len(row))
        for elem in range(len(row)):
            res.append(row[elem])
    if len(set(check_elem)) > 1:
        raise MyException()
    return res, separator_matrix, separator_line


a = Matrix([[1, 2, 3], [1, 4, 5]])
print(a)
print('#'*30)
b = Matrix([[6, 2, 5], [8, 14, 12]])
print(a + b)
print('#'*30)
c = Matrix([[6, 2, 5], [8, 14]])
print(a + c)
print('#'*30)
d = Matrix([[6, 2, 5], [8, 14, 34, 32]])
print(a + d)
print('#'*30)
e = Matrix([[6, 2, 5], [8, 14, "32"]])
print(a + e)
print('#'*30)
f = Matrix([[6, 2, 5], [8, 14, 32], [1, 2, 3]])
print(a + f)
print('#'*30)
print(d)
