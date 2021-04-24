"""
2.Реализовать класс Person, у которого должно быть два атрибута: age и name.
Также у него должен быть следующий набор методов:
    1.def know(self, another_person_object)
    который позволяет добавить другого человека в список знакомых (лист __friends (обязательно приватный атрибут)).
    2.def is_known(self, another_person_object)
    который возвращает знакомы ли два человека (True/False)
"""

import uuid


class Person:
    def __init__(self, age, name, _id):
        self.name = name
        self.age = age
        self._id = _id  # присвоение id для случая, если имена и возраст одинаковы
        self.__friends = {}  # словарь друзей объекта

    def know(self, other):
        self.__friends.setdefault(other._id, other)
        # добавляет в словарь объекта друга с id

    def is_known(self, other):
        return other._id in self.__friends
        # True если id друга есть в словаре __friends

    @property  # Из за этого декоратора мы не можем изменять лист друзей в этом методе
    def friends(self):
        return list(self.__friends.values())


person1 = Person(18, 'Oleg', _id=uuid.uuid4())
person2 = Person(20, 'Ivan', _id=uuid.uuid4())
person3 = Person(20, 'Ivan', _id=uuid.uuid4())

print(person1.is_known(person2))

person1.know(person2)
person1.know(person3)
print(person1.is_known(person2))
print(person1.friends)

