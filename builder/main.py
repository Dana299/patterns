from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class CarBuilder(ABC):
    """
    Интерфейс строителя определяет шаги конструирования,
    общие для всех видов строителей.
    """
    def __init__(self) -> None:
        self.car = Car()

    @abstractmethod
    def set_model(self):
        pass

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_color(self):
        pass

    def get_car(self):
        # метод получения результата можно
        # реализовать в конкретных строителях,
        # так как возвращаемые объекты
        # не обязаны иметь общий базовый класс, как в примере
        return self.car


class Car:
    """Класс, представляющий создаваемый объект."""
    def __init__(self):
        self.model: Optional[str] = None
        self.engine: Optional[str] = None
        self.color: Optional[str] = None

    def __str__(self):
        return f"{self.color} {self.model} with {self.engine} engine"


class SportsCarBuilder(CarBuilder):
    """Конкретные строители реализовывают по своему эти шаги."""
    def set_model(self):
        self.car.model = "Sports Car"

    def set_engine(self):
        self.car.engine = "V8"

    def set_color(self):
        self.car.color = "Red"


class SUVBuilder(CarBuilder):
    def set_model(self):
        self.car.model = "SUV"

    def set_engine(self):
        self.car.engine = "V6"

    def set_color(self):
        self.car.color = "Black"


class Director:
    """
    Директор определяет порядок вызова строительных шагов
    для производства той или иной конфигурации продуктов.
    """
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_car(self):
        self.builder.set_model()
        self.builder.set_engine()
        self.builder.set_color()

        return self.builder.get_car()


# Пример использования
if __name__ == "__main__":
    # клиент подаёт в конструктор директора
    # уже готовый объект-строитель,
    # и в дальнейшем данный директор использует только его;

    # возможно также подать строителя напрямую в строительный метод директора

    sports_car_builder = SportsCarBuilder()
    suv_builder = SUVBuilder()

    director = Director(sports_car_builder)
    sports_car = director.construct_car()
    print("Sports Car Details:", sports_car)

    director = Director(suv_builder)
    suv = director.construct_car()
    print("SUV Details:", suv)
