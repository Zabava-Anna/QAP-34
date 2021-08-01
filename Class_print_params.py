# Создайте класс любых геометрических фигур, где на выход мы получаем характеристики фигуры. Каждый экземпляр должен иметь атрибуты, 
# которые зависят от выбранной фигуры. Например, для прямоугольника это будут аргументы x, y, width и height.

# Кроме того вы должны иметь возможность передавать эти атрибуты при создании объекта класса.

# Создайте метод, который возвращает атрибуты вашей фигуры в виде строки. 
class Figures:
    def __init__(self, x, y, widht, height):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
    def params(self):
        return 'Figures ({0}, {1}, {2}, {3})'.format(self.x, self.y, self.widht, self.height)

Rectangle = Figures(5, 10, 50,100)
print(Rectangle.params())
