from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
# print(rect_1.get_area())
# print(rect_2.get_area())

sq_1 = Square(5)
sq_2 = Square(10)
# print(sq_1.get_area_square(), sq_2.get_area_square())

circle_1 = Circle(5)
circle_2 = Circle(10)

figures = [rect_1, rect_2, sq_1, sq_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())
