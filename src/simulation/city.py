# src/simulation/city.py
import datetime
import math
import random
from datetime import timedelta
from src.simulation.person import Person
# from src.utils.helpers import haversine_distance  # Import the haversine_distance function
# from shapely.geometry import Polygon
from geopy.distance import geodesic
import matplotlib.pyplot as plt


class City:
    """
    Class representing a city in the urban simulation.

    Attributes:
        id (int): The unique identifier of the city.
        population (int): The population of the city.
        coordinates_area (list of tuples): The area of the city.
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
            coordinates_area (list of tuples): The list of tuples of the coordinates of the city.
            gdp (float): The gdp of the city.
        """
        self.id = id
        self.population = population
        self.coordinates_area = coordinates_area
        self.gdp = gdp
        self.area = 0
        self.inhabitants_list = []
        self.building_list = []

    def compute_area(self):
        """
        Compute the area of the city based on the given coordinates.

        Args:
            coordinates_area (list of tuples): A list of tuples where each tuple contains the latitude and longitude in degrees decimal (DD).

        Returns:
            float: The computed area in square kilometers.
        """
        n = len(self.coordinates_area)
        if n < 3:
            raise ValueError("A polygon must have at least 3 vertices.")

        # Convert coordinates to a flat map using Geodesic distances
        distances = []
        for i in range(n):
            x = geodesic(self.coordinates_area[i], (self.coordinates_area[i][0], 0)).meters
            y = geodesic(self.coordinates_area[i], (0, self.coordinates_area[i][1])).meters
            distances.append((x, y))

        # Calculate area using the shoelace formula
        area = 0
        for i in range(n - 1):
            x_i, y_i = distances[i]
            x_ip1, y_ip1 = distances[i + 1]
            area += x_i * y_ip1 - y_i * x_ip1

        # Add the last vertex to the first
        x_n, y_n = distances[-1]
        x_1, y_1 = distances[0]
        area += x_n * y_1 - y_n * x_1

        self.area = abs(area) / 2  # The area is already in square meters
        return self.area / 1e6  # Convert to square kilometers

    @staticmethod
    def generate_city_boundary_coordinates(n, center_lat=45.75, center_lon=4.83, radius=0.01, perturbation=0.002):
        """
        Generates n coordinates around a center point to form a convex polygon representing the boundary of a city
        using the Jarvis March algorithm.

        Args:
            n (int): Number of boundary points to generate.
            center_lat (float): Latitude of the center point.
            center_lon (float): Longitude of the center point.
            radius (float): Maximum distance from the center point for the boundary points.
            perturbation (float): Maximum perturbation distance to add randomness to points.

        Returns:
            list: List of tuples representing the coordinates in decimal degrees.
        """
        points = []

        angle_increment = 2 * math.pi / n
        for i in range(n):
            angle = i * angle_increment
            distance = radius + random.uniform(-perturbation, perturbation)

            delta_lat = distance * math.cos(angle)
            delta_lon = distance * math.sin(angle)

            new_lat = center_lat + delta_lat
            new_lon = center_lon + delta_lon

            points.append((new_lat, new_lon))

        # Jarvis March algorithm to find the convex hull
        hull = []

        # Find the leftmost point
        l = min(points, key=lambda p: p[0])
        p = l
        while True:
            hull.append(p)
            q = points[0]
            for r in points:
                if (q == p) or (City.orientation(p, q, r) == 2):
                    q = r
            p = q
            if p == l:
                break

        return hull

    @staticmethod
    def orientation(p, q, r):
        """
        To find the orientation of the ordered triplet (p, q, r).
        The function returns:
        0 -> p, q and r are collinear
        1 -> Clockwise
        2 -> Counterclockwise
        """
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

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
        pass

    def plot_city(self):
        """
        Plot the city boundary using the coordinates in coordinates_area.
        """
        if not self.coordinates_area:
            raise ValueError("No coordinates available to plot.")

        # Extract latitude and longitude
        lats, lons = zip(*self.coordinates_area)

        # Plot the boundary
        plt.figure(figsize=(50, 50))
        plt.plot(lons + (lons[0],), lats + (lats[0],), marker='o')
        plt.fill(lons + (lons[0],), lats + (lats[0],), alpha=0.2)
        plt.title(f'City Boundary (City ID: {self.id})')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)
        plt.show()

    def __str__(self):
        return f'{self.id} {self.population} {self.area} {self.gdp}'


# Example usage
if __name__ == "__main__":

    # Example coordinates in degrees decimal
    coordinates1 = [
        (45.75194444, 4.83305556),
        (45.76166667, 4.83388889),
        (45.76138889, 4.84777778),
        (45.75250000, 4.84750000)
    ]

    plougastel = City(1, 0, [], 0)
    plougastel.coordinates_area = plougastel.generate_city_boundary_coordinates2(2057,
                                                                                 center_lat=45.75,
                                                                                 center_lon=4.83,
                                                                                 radius=0.01,
                                                                                 perturbation=0.00999999)

    print(plougastel.coordinates_area)
    plougastel.area = plougastel.compute_area()
    print(plougastel.area)

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
    print(plougastel)
    plougastel.plot_city()

"""
Note for later:
    - Addition of a list with the coordinates of the city's boundaries'
    - For now, we are handling coordinates in DD (decimal degrees) format, but we will incorporate a possible 
    switch to DMS (Degrees, Minutes, Seconds) format
    
"""
