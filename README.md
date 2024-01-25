# Паттерны проектирования

## Структурные паттерны

1. Адаптер

2. Мост

   Разделяет один или несколько классов на две отдельные иерархии — абстракцию и реализацию, позволяя изменять их независимо друг от друга. Абстракция будет делегировать работу одному из объектов реализаций, и их можно будет взаимозаменять, при условии что все они будут следовать общему интерфейсу. Клиентский код не имеет прямого доступа к объектам реализации и работает только с абстракциями.
3. Фасад
4. Заместитель (прокси)

   Позволяет подставлять вместо реальных объектов специальные объекты-заменители. Эти объекты перехватывают вызовы к оригинальному объекту, позволяя сделать что-то до или после передачи вызова оригиналу.

5. Легковес
6. Компоновщик

   Позволяет сгруппировать множество объектов в древовидную структуру, а затем работать с ней так, как будто это единичный объект.

## Поведенческие паттерны

7. Цепочка обязанностей

   Позволяет передавать запросы последовательно по цепочке обработчиков. Каждый последующий обработчик решает, может ли он обработать запрос сам и стоит ли передать запрос дальше по цепи.

8. Команда
9. Итератор
10. Посредник

    Позволяет уменьшить связанность множества
классов между собой, благодаря перемещению этих связей
в один класс-посредник.

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

## Сравнение паттернов

### **Мост VS Стратегия**

Оба построены на принципе композиции и имеют идентичную структуру, но предназначены для разных целей. Мост - структурное решение, позволяющее расширять класс в двух независимых плоскостях, а стратегия - поведенческий паттерн, который позволяет выполнять операцию различными способами и подменять этот способ во время выполнения программы.

### **Прокси VS Декоратор**

Прокси предоставляет клиенту тот же интерфейс, а декоратор - расширенный интерфейс. Декоратор используется для расширения функциональности, а прокси - как правило для ограничения доступа.
