from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Интерфейс транспорта объявляет операции, которые должны выполнять все
    конкретные виды транспорта.
    """
    @abstractmethod
    def deliver(self):
        pass


class Ship(Transport):
    def deliver(self):
        print("Доставка товара по морю.")


class Truck(Transport):
    def deliver(self):
        print("Доставка грузовиком по суше.")


class Logistic(ABC):
    """
    Класс объявляет фабричный метод, который должен возвращать
    объект класса Транспорт. Подклассы класса Логистика
    предоставляют реализацию этого метода.
    Основная обязанность класса заключается не в создании транспорта,
    обычно он содержит некоторую базовую бизнес-логику, которая основана на
    объектах Транспорта, возвращаемых фабричным методом.
    """
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()


class RoadLogistic(Logistic):
    """
    Конкретные классы логистики переопределяют фабричный метод
    для того, чтобы изменить тип результирующего вида транспорта.
    """
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Ship()


if __name__ == "__main__":
    sea_logistic = SeaLogistic()
    road_logistic = RoadLogistic()

    sea_logistic.plan_delivery()
    road_logistic.plan_delivery()
