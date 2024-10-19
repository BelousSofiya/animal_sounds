from unittest import TestCase
from animalSound import *


class GetTest(TestCase):

    def test_get_animal_success(self):
        expected = "bark"
        animal = get_animal({ "field1": "value1", "animal": "dog" })
        actual = animal.make_sound()
        self.assertEqual(expected, actual)

    def test_get_unknown_animal(self):
        expected = "do is unknown or absent"
        with self.assertRaises(TypeError) as exc:
            get_animal({"field1": "value1", "animal": "do"})
        self.assertEqual(exc.exception.__str__(), expected)

    def test_get_animal_not_exist(self):
        expected = "None is unknown or absent"
        with self.assertRaises(TypeError) as exc:
            get_animal({"field1": "value1"})
        self.assertEqual(exc.exception.__str__(), expected)