from __future__ import annotations

from abc import ABC, abstractmethod


class DBManager:
    """"
    Абстракция устанавливает интерфейс для «управляющей» части двух иерархий
    классов. Она содержит ссылку на объект из иерархии Реализации и делегирует
    ему всю настоящую работу.
    """
    def __init__(self, db: DatabaseImplementation):
        self.db = db

    def select_all(self):
        return self.db.select_all()


class DatabaseImplementation(ABC):

    @abstractmethod
    def select_all(self):
        pass


class MySQL(DatabaseImplementation):

    def select_all(self):
        print("Select query was executed with MySQL database.")


class PostgreSQL(DatabaseImplementation):
    def select_all(self):
        print("Select query was executed with PostgreSQL database.")


if __name__ == "__main__":
    mysql_db = MySQL()
    postgres_db = PostgreSQL()

    mysql_manager = DBManager(mysql_db)
    postgres_manager = DBManager(postgres_db)

    mysql_manager.select_all()
    postgres_manager.select_all()
