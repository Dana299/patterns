from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class User:
    is_admin: bool
    is_active: bool


class Post:
    _state = None

    def __init__(self, state: State, author: User) -> None:
        self.author = author
        self.change_state(state)

    def change_state(self, state: State):
        """
        Контекст позволяет изменять состояние во время выполнения программы.
        """
        self._state = state
        self._state.context = self

    def publish(self, *args, **kwargs) -> None:
        self._state.publish(*args, **kwargs)


class State(ABC):
    """
    Интерфейс состояния, объявляет методы которые
    должны реализовывать все конкретные состояния, а также
    предоставляет обратную ссылку на объект контекста, связанного
    с состоянием."""

    @property
    def context(self) -> Post:
        return self._context

    @context.setter
    def context(self, context: Post) -> None:
        self._context = context

    @abstractmethod
    def publish(self, *args, **kwargs) -> None:
        """Метод для публикации поста."""
        pass


class Draft(State):
    """Класс конкретного состояния поста в статусе черновика."""
    def publish(self, current_user: User) -> None:
        self.context.change_state(OnModeration())
        print("Пост переведен в статус `На модерации`.")


class OnModeration(State):
    """Класс конкретного состояния поста в статусе модерации."""
    def publish(self, current_user: User) -> None:
        if current_user.is_admin:
            self.context.change_state(Published())
            print("Пост прошел модерацию и опубликован.")
        else:
            print("Посты может модерировать только администратор.")


class Published(State):
    """Класс конкретного состояния поста в статусе `опубликовано`."""
    def publish(self, *args, **kwargs) -> None:
        print("Не произведено действий с постом, который уже опубликован.")


if __name__ == "__main__":
    admin = User(is_admin=True, is_active=True)
    common_user = User(is_admin=False, is_active=True)
    draft_post = Post(Draft(), common_user)
    draft_post.publish(current_user=common_user)
    moderation_post = Post(OnModeration(), common_user)
    moderation_post.publish(current_user=common_user)
    moderation_post.publish(current_user=admin)
    published_post = Post(Published(), common_user)
    published_post.publish(current_user=common_user)
