# Напишите код для описания геометрической фигуры. 
# Создайте класс «прямоугольник» с помощью метода  __init__(). На выходе в консоли вам необходимо получить длину и ширину с итоговыми значениями. 
class Rectangle:
    def __init__(self, l, w):
        self.lenght = l
        self.widht = w

    def enter_area(self):
        return "Длина: {0}, Ширина: {1}, Площадь прямоугольника: ".format(self.lenght, self.widht), self.lenght * self.widht

NewRectangle = Rectangle(5, 10)
print(NewRectangle.enter_area())
