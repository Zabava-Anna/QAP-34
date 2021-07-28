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
