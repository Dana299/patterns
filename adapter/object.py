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


class ChinaAdapter(RussianPlug):
    def __init__(self, chinese_plug: ChinesePlug):
        self.chinese_plug = chinese_plug

    def power_russian(self):
        self.chinese_plug.power_chinese()


def client_code(plug: RussianPlug):
    """
    Клиентский код, позволяющий подключить российскую
    вилку к российской розетке.
    """
    russian_socket = RussianSocket()
    russian_socket.connect(plug)


if __name__ == "__main__":
    chinese_plug = ChinesePlug()
    adapter = ChinaAdapter(chinese_plug)
    client_code(adapter)
