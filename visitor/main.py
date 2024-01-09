from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Figure(ABC):
    """
    Интерфейс объявляет метод accept,
    который в качестве аргумента принимает любой объект,
    реализующий интерфейс Visitor.
    """
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


"""
Конкретные классы реализуют метод
принятия посетителя, вызывая внутри тот метод посещения,
который соответствует типу этого класса.
"""


class Square(Figure):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_square(self)


class Circle(Figure):
    def __init__(self, radius: int):
        self.radius = radius

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_circle(self)


class Visitor(ABC):
    @abstractmethod
    def visit_square(self, square: Square) -> None:
        pass

    @abstractmethod
    def visit_circle(self, circle: Circle) -> None:
        pass


class AreaCalculator(Visitor):
    """
    Конкретный посетитель реализует
    какое-то поведение для всех типов элементов,
    которые можно подать через методы интерфейса посетителя.
    """
    def visit_square(self, square: Square):
        return square.x * square.y

    def visit_circle(self, circle: Circle):
        return circle.radius * circle.radius * 3.14


if __name__ == "__main__":
    # клиентский код может выполнять операции посетителя
    # над любым набором элементов, не выясняя конкретных классов
    figures: List[Figure] = [Square(1, 2), Circle(3)]
    area_calculator = AreaCalculator()
    for figure in figures:
        figure.accept(area_calculator)
