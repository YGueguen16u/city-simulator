# src/simulation/city.py
import datetime
import random
from datetime import timedelta

from src.simulation.person import Person


class City:

    def __init__(self, id, population, area, gdp):
        self.id = id
        self.population = population
        self.area = area
        self.gdp = gdp
        self.habitants = []

    def new_habitants(self, n: int):
        """
        A function which creates n new habitants with parameters define by probabilities.

        Args :
            n: number of habitants
        Return:
        """
        occupations = ['engineer', 'retiree', 'teacher', 'butcher', 'baker']
        occupation_weights = [0.6, 0.1, 0.1, 0.05, 0.15]

        for i in range(n):
            occupation = random.choices(occupations, weights=occupation_weights, k=1)[0]
            id = len(self.habitants) + 1
            birth_date = (datetime.date.today() - timedelta(days=random.randint(365 * 60, 365 * 90))
                          if occupation == 'retiree'
                          else datetime.date.today() - timedelta(days=random.randint(365 * 23, 365 * 65)))
            if occupation == 'engineer':
                income = random.randint(35000, 100000)
            elif occupation == 'teacher':
                income = random.randint(25000, 45000)
            elif occupation == 'butcher':
                income = random.randint(25000, 65000)
            elif occupation == 'baker':
                income = random.randint(25000, 65000)
            elif occupation == 'retiree':
                income = random.randint(18000, 60000)

            new_person = Person(id, birth_date, occupation, income)
            self.habitants.append(new_person)
        self.population += len(self.habitants)

    def __str__(self):
        return f'{self.id} {self.population} {self.area} {self.gdp}'


# Example usage
if __name__ == "__main__":
    Plougastel = City(1, 0, 177, 0)
    Plougastel.new_habitants(10000)
    Plougastel.gdp = sum(hab.income*12/4 for hab in Plougastel.habitants)

    # Define the start and end dates of the simulation
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2026, 1, 12)

    while start_date <= end_date:
        Plougastel.new_habitants(15)
        Plougastel.gdp = sum(hab.income*12/4 for hab in Plougastel.habitants)

        print(f"{Plougastel}, start {start_date}, gdp_per_captita {Plougastel.gdp/len(Plougastel.habitants)}")
        # Move to the next month
        next_month = start_date.month % 12 + 1
        next_year = start_date.year + (start_date.month // 12)
        start_date = start_date.replace(year=next_year, month=next_month, day=1)

    print(Plougastel.habitants[:10])