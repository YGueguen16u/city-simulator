# src/simulation/person.py
from datetime import date


class Person:
    """
    Class representing a person in the urban simulation.

    Attributes:
        id (int): The unique identifier of the person.
        birth_date (date): The birthdate of the person.
        occupation (str): The occupation or profession of the person.
        income (float): The annual income of the person.
        # social_class (str): The social class of the person.
        children (list): A list of children (instances of Person) associated with this person.
        savings (int): The savings of the person.
    """

    def __init__(self, id, birth_date, occupation, income):
        """
        Create a new instance of Person.
        Args:
            id (int): The unique identifier of the person.
            birth_date (date): The birthdate of the person.
            occupation (str): The occupation or profession of the person.
            income (float): The annual income of the person.
            # social_class (str): The social class of the person.
        """
        self.id = id
        self.birth_date = birth_date
        self.occupation = occupation
        self.income = income
        # self.social_class = social_class
        self.children = []
        self.savings = 0

    def calculate_age(self):
        """
        Calculate the age of the person based on the birth date.

        Returns:
            int: The age of the person.
        """
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))


    def add_child(self, child):
        """
        Adds a child to the person's list of children.

        Args:
            child (Person): The child to add.
        """
        self.children.append(child)

    def accountability(self):
        self.savings += (self.income/12) - 400 - 200

    def __repr__(self):
        """
        Represents the Person object as a string.

        Returns:
            str: Representation of the person.
        """
        age = self.calculate_age()
        return (f"Person(id={self.id}, age={age}, occupation={self.occupation}, "
                f"income={self.income})")
