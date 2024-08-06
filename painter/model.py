# TODO: Add code here
import math
import matplotlib.pyplot as plt


class point:
    def __int__(self, x:float, y:float):
        self.x: float = x
        self.y: float = y

class Circle:
    def __int__(self, center: point, radius: float):
        self.center: point = center
        self.radius: float = radius
    def area(self) -> float:
        area = math.pi * (self.radius **2)
    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return Circle with center at {self,(x, y) and radius r