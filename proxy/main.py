from abc import ABC, abstractmethod


class DataExtractor(ABC):
    """
    Интерфейс определяет структуру как для
    реального объекта, так и для прокси-объекта.
    С этим интерфейсом будет работать клиентский код.
    """

    @abstractmethod
    def select(self, key):
        pass


class DBExtractor(DataExtractor):
    """
    Реальный объект содержит некоторую базовую бизнес-логику.
    Как правило, реальные объекты способны выполнять некоторую
    полезную работу, которая может быть очень медленной.
    Заместитель может решить эти задачи без каких-либо изменений в коде
    реального объекта.
    """

    def select(self, key):
        print("Очень медленная операция загрузки данных из БД.")


class CacheProxy(DataExtractor):
    """
    Прокси-объект реализует тот же интерфейс, что и реальный объект.
    Прокси может выполнить одну из требуемых задач, а затем,
    в зависимости от результата, передать выполнение
    одноимённому методу в связанном объекте класса реального объекта.
    """

    def __init__(self, db_extractor: DBExtractor):
        self._db_extractor = db_extractor
        self.redis_storage = {}

    def select(self, key):
        result = self.redis_storage.get(key)
        if not result:
            print("Данные не обнаружены в кэше, иду в БД.")
            result = self._db_extractor.select(key)
        return result


def client_code(extractor: DataExtractor):
    """
    Клиентский код поддерживает интерфейс, который
    реализует как реальный объект, так и прокси.
    """
    key = "session"
    extractor.select(key)


if __name__ == "__main__":
    db_extractor = DBExtractor()
    redis = CacheProxy(db_extractor)
    client_code(db_extractor)

    client_code(redis)
