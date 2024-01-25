from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    Базовый класс Компонент объявляет общие операции как для простых, так и
    для сложных объектов структуры.
    """
    @abstractmethod
    def get_disk_usage(self) -> int:
        pass

    @abstractmethod
    def is_composite(self) -> bool:
        pass


class File(Component):
    """
    Конечный объект структуры не меет дочерних компонентов
    и выполняет сам фактическую работу.
    """

    def __init__(self, disk_usage: int) -> None:
        self._disk_usage = disk_usage

    def get_disk_usage(self):
        return self._disk_usage

    def is_composite(self):
        return False


class Directory(Component):
    """
    Класс директории может содержать внутри себя
    как простые, так и составные объекты (другие директории)
    и делегирует фактическую работу своим детям.
    """
    def __init__(self):
        self.children: List[Component] = []

    def is_composite(self):
        return True

    def add_child(self, child: Component):
        self.children.append(child)

    def remove_child(self, child: Component):
        self.children.remove(child)

    def get_disk_usage(self):
        res = 0
        for child in self.children:
            res += child.get_disk_usage()
        return res


if __name__ == '__main__':
    level_1_directory = Directory()
    file_1 = File(3)
    picture_1 = File(12)
    level_2_directory = Directory()
    file_2 = File(2)
    level_2_directory.add_child(file_2)
    level_1_directory.add_child(file_1)
    level_1_directory.add_child(picture_1)
    level_1_directory.add_child(level_2_directory)

    print(level_1_directory.get_disk_usage())
