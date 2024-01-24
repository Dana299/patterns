from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class User(ABC):
    def __init__(self, mediator: Mediator, name: str) -> None:
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, message: str, sender: User):
        pass


class Mediator(ABC):
    """
    Интерфейс посредника определяет метод,
    используемый компонентами для уведомления о
    различных событиях.
    """
    def notify(self, sender, event: str, *args, **kwargs):
        pass


class ConcreteUser(User):
    def send(self, message: str):
        self.mediator.notify(
            sender=self,
            event="send_message",
            message=message,
        )

    def receive(self, message: str, sender: User):
        print(
            f"User {self.name} received message `{message}` from {sender.name}."
        )


class ChatMediator(Mediator):
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, user: User):
        self.users.append(user)

    def notify(self, sender: User, event: str, *args, **kwargs):
        if event == "send_message":
            for user in self.users:
                message = kwargs.get("message", "")
                if sender is not user:
                    user.receive(message=message, sender=sender)


if __name__ == "__main__":
    chat_mediator = ChatMediator()
    alice = ConcreteUser(chat_mediator, "Alice")
    bob = ConcreteUser(chat_mediator, "Bob")
    george = ConcreteUser(chat_mediator, "George")
    dana = ConcreteUser(chat_mediator, "Dana")
    mike = ConcreteUser(chat_mediator, "Mike")
    chat_mediator.add_user(george)
    chat_mediator.add_user(dana)
    chat_mediator.add_user(mike)
    chat_mediator.add_user(bob)
    chat_mediator.add_user(alice)
    dana.send("Hello everyone!")
