# from turtle import Turtle, Screen
# my_screen = Screen()
# Seabela = Turtle()
# print(my_screen.canvwidth)
# Seabela.shape('turtle')
# Seabela.color('purple')
# Seabela.forward(100)
# Seabela.right(90)
# Seabela.forward(100)
# Seabela.right(90)
# Seabela.forward(100)
# Seabela.right(90)
# Seabela.forward(200)
# Seabela.home()
#
#
# my_screen.exitonclick()

class Robot:
    """This class implements a robot"""
    def __init__(self, name, year):
        self.name = name
        self.year = year

r1 = Robot('R1', 2023)
print(r1.__doc__)
print(f'Robot name: {r1.name}')
print(r1.__doc__)