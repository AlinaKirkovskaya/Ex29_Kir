from abc import ABC, abstractmethod
import math


# Базовий клас для всіх фігур
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


# Інтерфейс для малювання фігур
class IDrawable(ABC):
    @abstractmethod
    def draw(self):
        pass


# Клас для кола
class Circle(Shape, IDrawable):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

    def draw(self):
        print("Drawing a circle")


# Клас для квадрата
class Square(Shape, IDrawable):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def draw(self):
        print("Drawing a square")


# Клас для трикутника
class Triangle(Shape, IDrawable):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def draw(self):
        print("Drawing a triangle")


# Використання поліморфізму для обчислення площі та виклику методу draw() зі списку фігур
def main():
    shapes = [
        Circle(radius=5),
        Square(side=4),
        Triangle(base=3, height=6)
    ]

    for shape in shapes:
        print(f"Area: {shape.calculate_area()}")
        shape.draw()


if __name__ == "__main__":
    main()