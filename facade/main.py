class BIOS:
    def start_post(self):
        """Начинает power-on-self-test."""
        print("Все компоненты исправны.")

    def find_bootloader(self):
        print("Код загрузичка найден и загружен в оперативную память.")


class BootLoader:
    def load_kernel(self):
        print("Ядро операционной системы загружено в оперативную память.")


class OS:
    def start_system_services(self):
        print("Системные службы успешно запущены.")

    def load_drivers(self):
        print("Драйверы загружены.")

    def clean_ram(self):
        print("Оперативная память очищена.")

    def stop_system_services(self):
        print("Все системные службы остановлены.")


class ComputerFacade:
    def __init__(self) -> None:
        self.bios = BIOS()
        self.bootloader = BootLoader()
        self.os = OS()

    def turn_on(self):
        self.bios.start_post()
        self.bios.find_bootloader()
        self.bootloader.load_kernel()
        self.os.start_system_services()
        self.os.load_drivers()

    def turn_off(self):
        self.os.stop_system_services()
        self.os.clean_ram()


def start_working_day(facade: ComputerFacade):
    facade.turn_on()


if __name__ == '__main__':
    facade = ComputerFacade()
    start_working_day(facade)
