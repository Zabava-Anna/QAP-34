class Rectangle:
    def __init__(self, l, w):
        self.lenght = l
        self.widht = w

    def enter_area(self):
        return "Длина: {0}, Ширина: {1}, Площадь прямоугольника: ".format(self.lenght, self.widht), self.lenght * self.widht

NewRectangle = Rectangle(5, 10)
print(NewRectangle.enter_area())
