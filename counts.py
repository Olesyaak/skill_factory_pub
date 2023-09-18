from basic_classes import Rectangle, Squere, Circle

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.get_area())
print(rect_2.get_area())

squere_1 = Squere(5)
squere_2 = Squere(12)

print(squere_1.get_area())
print(squere_2.get_area())

circle_1 = Circle(10)
circle_2 = Circle(6)

print(circle_1.get_area())
print(circle_2.get_area())

figures = [rect_1, rect_2, squere_1, squere_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Squere):
        print(figure.get_area())
    elif isinstance(figure, Circle):
        print(figure.get_area())
    else:
        print(figure.get_area())
