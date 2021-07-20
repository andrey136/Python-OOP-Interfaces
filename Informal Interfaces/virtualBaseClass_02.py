def main() -> None:
    print(issubclass(Employee, PersonSuper))
    print(issubclass(Employee, Person))
    print(issubclass(Friend, Person))


class PersonMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and
                callable(subclass.name) and
                hasattr(subclass, 'age') and
                callable(subclass.age))


class PersonSuper:
    def name(self) -> str:
        ...

    def age(self) -> int:
        ...


class Person(metaclass=PersonMeta):
    ...


class Employee(PersonSuper):
    ...


class Friend:
    def name(self) -> str:
        ...

    def age(self) -> int:
        ...


if __name__ == '__main__':
    main()
