from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, List


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков
    и метод для выполнения запроса.
    """
    @abstractmethod
    def set_next_handler(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class BaseHandler(Handler):
    """
    Базовый класс обработчика содержит метод построения цепочки по умолчанию.
    """

    _next_handler = None

    def set_next_handler(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request) -> Optional[str]:
        if self._next_handler is not None:
            self._next_handler.handle(request)
        return None


class HostsFileHandler(BaseHandler):
    """
    Конкретный обработчик для поиска адресов в файле hosts.
    Все Конкретные Обработчики либо обрабатывают запрос, либо передают его
    следующему обработчику в цепочке.
    """
    def __init__(self, hosts_file_path):
        self.hosts_file_path = hosts_file_path

    def handle(self, request):
        ip_address = self.lookup_in_hosts_file(request)
        if ip_address:
            print(
                f"Address {request} found in hosts file with IP: {ip_address}"
            )
        else:
            super().handle(request)

    def lookup_in_hosts_file(self, address):
        hosts_data = {
            'localhost': '127.0.0.1',
        }
        return hosts_data.get(address)


class DnsServerHandler(BaseHandler):
    def handle(self, address):
        ip_address = self.lookup_in_dns_server(address)
        if ip_address:
            print(
                f"Address {address} resolved by DNS server with IP: {ip_address}"
            )
        else:
            print(f"Address {address} not found in DNS server")

    def lookup_in_dns_server(self, address):
        # В реальном приложении здесь была бы логика запроса к DNS-серверу
        dns_data = {
            'www.example.com': '203.0.113.1',
            'www.example.org': '203.0.113.2'
        }
        return dns_data.get(address)


def client_code(handler: Handler, requests: List[str]):
    """
    Обычно клиентский код приспособлен для работы с единственным
    обработчиком. В большинстве случаев клиенту даже неизвестно, что этот
    обработчик является частью цепочки.
    """
    for request in requests:
        handler.handle(request)


if __name__ == "__main__":
    hosts_handler = HostsFileHandler('/etc/hosts')
    dns_handler = DnsServerHandler()
    hosts_handler.set_next_handler(dns_handler)
    requests = ["localhost", "www.example.com", "www.example.org",]
    client_code(hosts_handler, requests)
