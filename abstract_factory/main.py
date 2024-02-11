from __future__ import annotations

import platform
from abc import ABC, abstractmethod


class TextField(ABC):
    """
    Каждый отдельный продукт семейства продуктов должен иметь базовый
    интерфейс. Все вариации продукта должны реализовывать этот интерфейс.
    """
    @abstractmethod
    def render(self):
        pass


class Button(ABC):
    @abstractmethod
    def render(self):
        pass


class CheckBox(ABC):
    @abstractmethod
    def render(self):
        pass


class WinButton(Button):
    def render(self):
        print("Windows button")


class WinCheckBox(CheckBox):
    def render(self):
        print("Windows checkbox")


class WinTextField(TextField):
    def render(self):
        print("Windows textfield")


class LinuxButton(Button):
    def render(self):
        print("Linux button")


class LinuxCheckBox(CheckBox):
    def render(self):
        print("Linux checkbox")


class LinuxTextField(TextField):
    def render(self):
        print("Linux textfield")


class GUIFactory(ABC):
    """
    Интерфейс Абстрактной Фабрики объявляет набор методов, которые
    возвращают различные абстрактные продукты. Эти продукты называются
    семейством и связаны темой или концепцией высокого уровня. Продукты одного
    семейства обычно могут взаимодействовать между собой. Семейство продуктов
    может иметь несколько вариаций, но продукты одной вариации несовместимы с
    продуктами другой.
    """
    @abstractmethod
    def create_text_field(self) -> TextField:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass

    @abstractmethod
    def create_button(self) -> Button:
        pass


class WinGUIFactory(GUIFactory):
    """
    Конкретная Фабрика производит семейство продуктов одной вариации.
    Фабрика гарантирует совместимость полученных продуктов.
    """
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> CheckBox:
        return WinCheckBox()

    def create_text_field(self) -> TextField:
        return WinTextField()


class LinuxGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> CheckBox:
        return LinuxCheckBox()

    def create_text_field(self) -> TextField:
        return LinuxTextField()


def client_code(gui_factory: GUIFactory):
    """
    Клиентский код не зависит от конкретных
    фабрик и элементов интерфейса, он общается
    с ними через абстрактные интерфейсы.
    """
    button = gui_factory.create_button()
    button.render()
    checkox = gui_factory.create_checkbox()
    checkox.render()
    textfield = gui_factory.create_text_field()
    textfield.render()


if __name__ == "__main__":
    os_type = platform.system()
    if os_type == "Windows":
        gui_factory = WinGUIFactory()
    elif os_type == "Linux":
        gui_factory = LinuxGUIFactory()
    client_code(gui_factory)
