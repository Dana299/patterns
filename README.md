# Паттерны проектирования

## Структурные паттерны

1. Адаптер

2. Мост
3. Фасад
4. Заместитель
5. Легковес
6. Компоновщик

## Поведенческие паттерны

7. Цепочка обязанностей
8. Команда
9. Итератор
10. Посредник
11. Снимок
12. Наблюдатель
13. Состояние

    Позволяет объектам менять поведение в зависимости от состояния. Когда код класса содержит множество похожих друг на друга блоков "if-else", целесообразно логику каждой ветки вынести в объект состояния, на который будет ссылаться первоначальный объект и которому он будет делегировать часть работы.
14. Стратегия

    Определяет семейство схожих алгоритмов, которые часто изменяются или расширяются, и помещает их в собственные классы. Выполнение алгоритма класс будет делегировать объекту стратегии.
15. Шаблонный метод
16. Посетитель

    Позволяет добавлять в программу новые операции, не изменяя класс объектов, над которыми эти операции могут выполняться.

## Порождающие паттерны

17. Фабричный метод
18. Абстрактная фабрика
19. Строитель
20. Прототип
21. Синглтон