# src/simulation/model.py

from src.simulation.person import Person


class SimulationModel:
    """
    Simulation model for managing and evolving people in a city.

    Attributes:
        people (list): List of people (instances of Person) in the simulation.
    """

    def __init__(self):
        """
        Initializes a new instance of the SimulationModel class.
        """
        self.people = []

    def add_person(self, person):
        """
        Adds a person to the simulation.

        Args:
            person (Person): The person to add.
        """
        self.people.append(person)

    def step(self):
        """
        Performs a single simulation step.
        """
        for person in self.people:
            # Simulation logic for each person
            pass

    def run(self, steps):
        """
        Runs the simulation for a given number of steps.

        Args:
            steps (int): The number of simulation steps to run.
        """
        for _ in range(steps):
            self.step()


# Example usage
if __name__ == "__main__":
    model = SimulationModel()

    person1 = Person(id=1, age=30, occupation="Teacher", income=30000, social_class="Middle")
    person2 = Person(id=2, age=45, occupation="Engineer", income=50000, social_class="Upper")

    model.add_person(person1)
    model.add_person(person2)

    model.run(steps=10)
