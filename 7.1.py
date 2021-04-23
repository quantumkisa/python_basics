class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        for i in range(len(self.list)):
            if i > 0:
                print(end="\n")
            for el in self.list[i]:
                print(el, end=" ")

    def __add__(self, other):
        for i in range(len(self.list)):
            if i > 0:
                print(end="\n")
            for j in range(len(self.list[i])):
                print(self.list[i][j] + other.list[i][j], end=' ')

list_1 = [[1, 2], [3, 4], [5, 6]]
list_2 = [[1, 2], [3, 4], [5, 6]]
ob_1 = Matrix(list_1)
ob_2 = Matrix(list_2)
print(ob_1 + ob_2)