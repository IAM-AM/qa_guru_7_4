from math import pi
import random


def test_greeting():
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = 2 * (a + b)
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a * b
    assert area == 200


def test_circle():
    r = 23
    # TODO сосчитайте площадь
    area = pi * (r ** 2)
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 2 * pi * r
    assert length == 144.51326206513048


def test_random_list():
    # TODO создайте список

    l = [random.randrange(1, 100) for i in range(10)]
    l.sort()
    sorted(l)  # as an option
    print(l)

    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    # NOTE: Option 1

    l1 = []
    for i in l:
        if i not in l1:
            l1.append(i)
    l = l1
    print(f'Updated list without duplicates = {l}')

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # NOTE: Option 2
    # l2 = []
    # [l2.append(i) for i in l if i not in l2]
    # l = l2
    # print(l2)

    # NOTE: Option 3
    # l3 = list(set(l))
    # l = l3
    # print(l3)

    # NOTE: Option 4
    # for i in l:
    #     if l.count(i) > 1:
    #         l.remove(i)
    # print(l)


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    # NOTE: Option 1
    d = dict(zip(first, second))

    # NOTE: Option 2
    d1 = {k: v for k, v in zip(first, second)}
    print(d)
    print(d1)
    print(d.values())

    assert isinstance(d, dict)
    assert len(d) == 5
