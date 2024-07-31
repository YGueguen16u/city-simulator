# tests/test_simulation.py

import unittest
from src.simulation.person import Person


class TestPerson(unittest.TestCase):
    """
    Unit tests for the Person class.
    """

    def test_person_creation(self):
        """
        Tests the creation of a Person instance.
        """
        person = Person(id=1, age=30, occupation="Teacher", income=30000, social_class="Middle")
        self.assertEqual(person.id, 1)
        self.assertEqual(person.age, 30)
        self.assertEqual(person.occupation, "Teacher")
        self.assertEqual(person.income, 30000)
        self.assertEqual(person.social_class, "Middle")

    def test_add_child(self):
        """
        Tests adding a child to a Person instance.
        """
        parent = Person(id=1, age=30, occupation="Teacher", income=30000, social_class="Middle")
        child = Person(id=2, age=5, occupation=None, income=0, social_class="Middle")
        parent.add_child(child)
        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.children[0], child)


if __name__ == "__main__":
    unittest.main()
