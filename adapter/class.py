class RussianPlug:
    """
    Класс представления российской вилки, которая подходит только к
    российской розетке.
    Target-класс, который работает с клиентским кодом.
    """
    def power_russian(self):
        print("Выполнено подключение к российской розетке.")


class ChinesePlug:
    """
    Класс представления китайской вилки,
    которая не подходит к российской розетке.

    Класс, который будем адаптировать.
    """
    def power_chinese(self):
        print("Выполнено подключение китайской вилки к китайской розетке.")


class RussianSocket:
    """
    Класс представления розетки российского типа.
    """
    def connect(self, plug: "RussianPlug"):
        plug.power_russian()


class ChineseSocket:
    """
    Класс представления розетки китайского типа.
    """
    def connect(self, plug: ChinesePlug):
        plug.power_chinese()


class ChinaAdapter(RussianPlug, ChinesePlug):
    """
    Адаптер становится совместимым благодаря
    множественному наследованию с обоими интерфейсами -
    с тем, с которым работает клиентский код, и с тем,
    который хотим под него адаптировать.
    """

    def power_russian(self):
        self.power_chinese()


def client_code(plug: RussianPlug):
    """
    Клиентский код, позволяющий подключить российскую
    вилку к российской розетке.
    """
    russian_socket = RussianSocket()
    russian_socket.connect(plug)


if __name__ == "__main__":
    chinese_plug = ChinesePlug()
    adapter = ChinaAdapter()
    client_code(adapter)
