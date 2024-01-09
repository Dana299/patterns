from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import List, NamedTuple


class TransportType(Enum):
    TAXI = "taxi"
    BUS = "bus"
    TRAM = "tram"
    SUBWAY = "subway"
    ON_FOOT = "on_foot"


class Coordinate(NamedTuple):
    x: int
    y: int


@dataclass
class RouteStep:
    transport_type: TransportType
    way: List[Coordinate]
    travel_time: int
    fare: int


class Navigator:
    """
    Контекст определяет интерфейс для клиента.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Контекст принимает стратегию через конструктор, а также
        предоставляет сеттер для её изменения во время выполнения.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Контекст хранит ссылку на один из объектов Стратегии
        и работает со всеми стратегиями через общий интерфейс.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def build_optimal_route(
        self,
        start_point: Coordinate,
        destination_point: Coordinate,
        max_travel_time: int
    ) -> None:
        """
        Навигатор делегирует работу по построению маршрута стратегии
        и передает ей координаты пункта отправления,
        пункта назначения и максимальное время в пути.
        """
        result = self.strategy.build_route(start_point, destination_point)
        if sum(step.travel_time for step in result) > max_travel_time:
            print("Построенный пеший маршрут занимает больше установленного времени.")


class Strategy(ABC):
    """
    Интерфейс Стратегии объявляет операции, общие для всех поддерживаемых
    версий некоторого алгоритма.

    Контекст использует этот интерфейс для вызова алгоритма, определённого
    Конкретными Стратегиями.
    """

    @abstractmethod
    def build_route(
        self,
        start_point: Coordinate,
        destination_point: Coordinate,
        **kwargs
    ) -> List[RouteStep]:
        pass


class WalkingRouteBuilder(Strategy):
    def build_route(
        self,
        start_point: Coordinate,
        destination_point: Coordinate,
        **kwargs
    ) -> List[RouteStep]:
        # какой-то алгоритм построения пешего маршрута
        return [
            RouteStep(
                transport_type=TransportType.ON_FOOT,
                way=[start_point, destination_point],
                travel_time=28,
                fare=0
            )
        ]


class PublicTransportRouteBuilder(Strategy):
    def build_route(
        self,
        start_point: Coordinate,
        destination_point: Coordinate,
        **kwargs
    ) -> List[RouteStep]:
        # какой-то алгоритм построения маршрута на общественном транспорте
        return [
            RouteStep(
                transport_type=TransportType.BUS,
                way=[start_point, Coordinate(5, 5)],
                travel_time=7,
                fare=44
            ),
            RouteStep(
                transport_type=TransportType.TRAM,
                way=[Coordinate(5, 5), destination_point],
                travel_time=10,
                fare=44
            )
        ]


if __name__ == "__main__":
    # Клиентский код выбирает конкретную стратегию и передаёт её в контекст.
    # Клиент должен знать о различиях между стратегиями, чтобы сделать
    # правильный выбор.
    navigator = Navigator(WalkingRouteBuilder())

    print("Навигатор будет строить пешие маршруты.")
    optimal_route = navigator.build_optimal_route(
        start_point=Coordinate(0, 0),
        destination_point=Coordinate(10, 10),
        max_travel_time=20
    )
    print("Навигатор будет строить маршруты на общественном транспорте.")
    navigator.strategy = PublicTransportRouteBuilder()
    optimal_route = navigator.build_optimal_route(
        start_point=Coordinate(0, 0),
        destination_point=Coordinate(10, 10),
        max_travel_time=20
    )
