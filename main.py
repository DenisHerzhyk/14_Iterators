# 1).

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        return self.get_square() + other.get_square()

    def __mul__(self, n):
        return Rectangle(self.width, self.height) * n

    def __str__(self):
        return "Rectangle ({}, {})".format(self.width, self.height)


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1.get_square())  # 8
print(r2.get_square())  # 18

r3 = r1 + r2
print(r3)  # 26

r4 = r1.get_square() + 4
print(r4)  # 12

r5 = r1.get_square() * 3
print(r5)  # 24

print(r1 == r2)  # False
print(r1 == Rectangle(2, 4))  # True


# 2).

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_fraction(self):
        return self.a, self.b

    def __mul__(self, other):
        return self.get_fraction()[0] * other, self.get_fraction()[1]

    def __add__(self, other):
        return self.get_fraction()[0] + other * self.get_fraction()[1], self.get_fraction()[1]

    def __sub__(self, other):
        return self.get_fraction()[0] - other * self.get_fraction()[1], self.get_fraction()[1]

    def __eq__(self, other):
        return self.get_fraction() == other

    def __gt__(self, other):
        return self.get_fraction() > other

    def __lt__(self, other):
        return self.get_fraction() < other

    def __str__(self):
        return f"Fraction: {self.a}/{self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b.get_fraction()[1] * f_a.get_fraction()[0] + f_a.get_fraction()[1] * f_b.get_fraction()[0], f_a.get_fraction()[
    1] * f_b.get_fraction()[1]
print(f_c)  # Fraction: 21/18

f_d = f_b.get_fraction()[0] * f_a.get_fraction()[0], f_a.get_fraction()[1] * f_b.get_fraction()[1]
print(f_d)  # Fraction: 6/18

f_e = f_a.get_fraction()[0] * f_b.get_fraction()[1] - f_b.get_fraction()[0] * f_a.get_fraction()[1], f_a.get_fraction()[
    1] * f_b.get_fraction()[1]
print(f_e)  # Fraction: 3/18

print(f_d < f_c)  # True
print(f_d > f_e)  # True
print(f_a == f_d)  # False


# 3).

class Fibonacci:
    def __init__(self, limit):
        self.limit = limit

    def add(self):
        list = []
        a, b = 0, 1
        while a < self.limit:
            list.append(a)
            a, b = b, a + b
        return list


print(Fibonacci(100).add())


# 4).

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __iter__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                yield self.matrix[i][j]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for element in Matrix(matrix):
    print(element)


# 5).

class Pairs:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def generate(self):
        for i, j in zip(self.list1, self.list2):
            yield i, j


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
pairs = Pairs(list1, list2)
for i, j in pairs.generate():
    print(f"({i},{j})")


# 6).

# 1.
class Files:
    def __init__(self, file1, file2, file3):
        self.file1 = file1
        self.file2 = file2
        self.file3 = file3

    def open_read(self):
        read1 = open(self.file1, 'r', encoding="utf-8")
        yield read1.read()
        read2 = open(self.file2, 'r', encoding="utf-8")
        yield read2.read()
        read3 = open(self.file3, 'r', encoding="utf-8")
        yield read3.read()


for file_content in Files("file1.txt", "file2.txt", "file3.txt").open_read():
    print(file_content)


# 2.
class Files:
    def __init__(self, file1, file2, file3):
        self.files = [file1, file2, file3]

    def __iter__(self):
        self.current_file = 0
        return self

    def __next__(self):
        if self.current_file < len(self.files):
            with open(self.files[self.current_file], "r", encoding="utf-8") as f:
                content = f.read()
            self.current_file += 1
            return content
        else:
            raise StopIteration


for file_content in Files("file1.txt", "file2.txt", "file3.txt"):
    print(file_content)
