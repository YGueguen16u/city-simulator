# src/simulation/city.py

import datetime
import random
from datetime import timedelta
from src.simulation.person import Person
from src.utils.helpers import haversine_distance  # Import the haversine_distance function
from shapely.geometry import Polygon


class City:
    """
    Class representing a city in the urban simulation.

    Attributes:
        id (int): The unique identifier of the city.
        population (int): The population of the city.
        coordinates_area (float): The area of the city.
        gdp (float): The gdp of the city.
        inhabitants_list (list): A list of the id of the inhabitants of the city.
        building_list (list): A list of buildings in the city.

    """

    def __init__(self, id, population, coordinates_area, gdp):
        """
        Create a new instance of City.
        Args:
            id (int): The unique identifier of the city.
            population (int): The population of the city.
            coordinates_area (list): The list of tuples of the coordinates of the city.
            gdp (float): The gdp of the city.
        """
        self.id = id
        self.population = population
        self.coordinates_area = coordinates_area
        self.gdp = gdp
        self.area = 0
        self.inhabitants_list = []
        self.building_list = []

    def compute_area(self, coordinates_area):
        """
        Compute the area of the city based on the given coordinates.

        Args:
            coordinates_area (list of tuples): A list of tuples where each tuple contains the latitude and longitude in degrees decimal (DD).

        Returns:
            float: The computed area in square kilometers.
        """
        if len(coordinates_area) < 3:
            raise ValueError("At least three coordinates are required to compute an area.")

        # Convert coordinates to a Polygon and calculate the area
        polygon = Polygon(coordinates_area)
        area = polygon.area  # The area is returned in square degrees

        # Convert square degrees to square kilometers
        # This conversion is approximate as it depends on the location on Earth
        # 1 degree of latitude is approximately 111 km
        area_km2 = area * (111 ** 2)
        return area_km2

    def new_inhabitants(self, n: int):
        """
        A function which creates n new inhabitants with parameters define by probabilities.

        Args :
            n: number of inhabitants
        Return:
        """
        occupations = ['engineer', 'retiree', 'teacher', 'butcher', 'baker']
        occupation_weights = [0.6, 0.1, 0.1, 0.05, 0.15]
        income = 0

        for i in range(n):
            occupation = random.choices(occupations, weights=occupation_weights, k=1)[0]
            id_person = len(self.inhabitants_list) + 1
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

            new_person = Person(id_person, birth_date, occupation, income)
            self.inhabitants_list.append(new_person)
        self.population += len(self.inhabitants_list)

    def new_building(self, n: int, coordinates: list):
        """
        A function which creates n new buildings
        Args :
            n: number of buildings
            coordinates (list): A list of tuples of the coordinates and elevation of the area of the buildings.
        Return:

        """

    def __str__(self):
        return f'{self.id} {self.population} {self.area} {self.gdp}'


# Example usage
if __name__ == "__main__":
    def generate_coordinates_for_building(n):
        pass

    plougastel = City(1, 0, 177, 0)
    plougastel.new_inhabitants(10000)
    plougastel.gdp = sum(hab.income * 12 / 4 for hab in plougastel.inhabitants_list)

    # Define the start and end dates of the simulation
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2026, 1, 12)

    while start_date <= end_date:
        plougastel.new_inhabitants(15)
        plougastel.gdp = sum(hab.income * 12 / 4 for hab in plougastel.inhabitants_list)

        print(f"{plougastel}, start {start_date}, gdp_per_captita {plougastel.gdp / len(plougastel.inhabitants_list)}")
        # Move to the next month
        next_month = start_date.month % 12 + 1
        next_year = start_date.year + (start_date.month // 12)
        start_date = start_date.replace(year=next_year, month=next_month, day=1)

    print(plougastel.inhabitants_list[:10])


"""
Note for later:
    - Addition of a list with the coordinates of the city's boundaries'
    - For now, we are handling coordinates in DD (decimal degrees) format, but we will incorporate a possible 
    switch to DMS (Degrees, Minutes, Seconds) format
    
"""