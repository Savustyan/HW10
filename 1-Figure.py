"""
1.Реализовать класс фигуры. На основе фигуры реализовать класс треугольника, квадрата и прямоугольника с
методами подсчета площади и периметра. Методы должны возвращать (return) значение, а не принтить (это важно)
"""


class Figure:

    def cal_perimetr(self):
        raise NotImplementedError

    def cal_area(self):
        raise NotImplementedError


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        assert isinstance(side_a, int), 'Переменная должна быть типа int'
        assert isinstance(side_b, int), 'Переменная должна быть типа int'
        assert isinstance(side_c, int), 'Переменная должна быть типа int'
        self._validate_triangle(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _validate_triangle(self, side_a, side_b, side_c):
        assert (side_a >= 0), 'Переменная должна быть больше 0'
        assert (side_b >= 0), 'Переменная должна быть больше 0'
        assert (side_c >= 0), 'Переменная должна быть больше 0'
        assert ((side_a + side_b > side_c) and (side_b + side_c > side_a) and (side_a + side_c > side_b)), 'Невозможно'
        pass

    def cal_perimetr(self):
        return self.side_a + self.side_b + self.side_c

    def cal_area(self):
        per = self.cal_perimetr() / 2
        return (per * (per - self.side_a) * (per - self.side_b) * (per - self.side_c)) ** 0.5


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        assert isinstance(side_a, int), 'Переменная должна быть типа int'
        assert isinstance(side_b, int), 'Переменная должна быть типа int'
        self._validate_rectangle(side_a, side_b)
        self.side_a = side_a
        self.side_b = side_b

    def _validate_rectangle(self, side_a, side_b):
        assert (side_a >= 0), 'Переменная должна быть больше 0'
        assert (side_b >= 0), 'Переменная должна быть больше 0'
        assert (side_a != side_b), 'Это квадрат'
        pass

    def cal_perimetr(self):
        return (self.side_a + self.side_b) * 2

    def cal_area(self):
        return self.side_a * self.side_b


class Square(Figure):
    def __init__(self, side_a):
        assert isinstance(side_a, int), 'Переменная должна быть типа int'
        self._validate_square(side_a)
        self.side_a = side_a

    def _validate_square(self, side_a):
        assert (side_a >= 0), 'Переменная должна быть больше 0'
        pass

    def cal_area(self):
        return self.side_a ** 2

    def cal_perimetr(self):
        return self.side_a * 4


print('Периметр треугольника:', Triangle.cal_perimetr(Triangle(7, 5, 3)))
print('Площадь треугольника:', Triangle.cal_area(Triangle(7, 5, 3)))

print('Периметр прямоугольника:', Rectangle.cal_perimetr(Rectangle(7, 5)))
print('Площадь прямоугольника:', Rectangle.cal_area(Rectangle(7, 5)))

print('Периметр квадрата:', Square.cal_perimetr(Square(7)))
print('Площадь квадрата:', Square.cal_area(Square(7)))

