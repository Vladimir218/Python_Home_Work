from itertools import zip_longest


class Matrix:

    def __init__(self, *args):
        self.n = max(map(len, args))
        self.m = len(args)
        self.args = args
        self.matr = self.get_matrix()

    def get_matrix(self):
        return [list(_tuple) for _tuple in list(zip(*zip_longest(*self.args, fillvalue=0)))]

    def __str__(self):
        self.max_len_el = max([len(str(el)) for matr_str in self.matr for el in matr_str])
        self.matrix_print = ""
        for matr_str in self.matr:
            self.matrix_print += "\n"
            for el in matr_str:
                self.matrix_print += str(el) + " " * (self.max_len_el - len(str(el)) + 1)
        return self.matrix_print

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            return f"некорректный размер матриц"
        else:
            return Matrix(*[[self.matr[i][j] + other.matr[i][j] for j in range(self.n)] for i in range(self.m)])


matrix1 = Matrix([-12, 8, 8, 8, 9, 7, 5, 4], [3, 44444, 5], [5, 6, 7, 8, 9])
matrix2 = Matrix([1, 1, 1, 1, 1, 1, 1, 0], [3, 44444, 5], [5, 5, 4])
print(matrix1)
print(matrix1 + matrix2)
