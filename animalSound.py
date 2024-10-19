import json
from abc import ABC


class AbstractAnimal(ABC):
    def make_sound(self):
        pass


class Dog(AbstractAnimal):
    def make_sound(self):
        return "bark"


class Cat(AbstractAnimal):
    def make_sound(self):
        return "meow"


class Cow(AbstractAnimal):
    def make_sound(self):
        return "moo"


class Rat(AbstractAnimal):
    def make_sound(self):
        return "pipi"


class Alien(AbstractAnimal):
    def make_sound(self):
        return "KILL"


def get_animal_from_file(path):
    with open('test.json', 'r') as file:
        data = json.load(file)
        return data


def get_animal(data) -> AbstractAnimal:
    mapping = {
        "dog": Dog,
        "cat": Cat,
        "cow": Cow,
        "rat": Rat,
        "alien": Alien
    }
    animal = data.get('animal')
    try:
        return mapping[animal]()
    except KeyError as e:
        raise TypeError(f"{animal} is unknown or absent")


animal_data = get_animal_from_file('test.json')
animal = get_animal(animal_data)
print(animal.make_sound())
