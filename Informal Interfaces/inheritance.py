from abc import ABC, abstractmethod, ABCMeta


def main() -> None:
    jack = Dog('Jack', 4)
    print(jack)
    print(jack.speak('MOOOOO\n'))

    sara = Labrador('Sara', 3)
    print(sara)
    print(sara.speak())

    print('\n')
    print(isinstance(sara, Labrador))
    print(isinstance(sara, Dog))


class Dog(ABC):
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old!'

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class Labrador(Dog):
    def speak(self, sound='Auf'):
        return super().speak(sound)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
