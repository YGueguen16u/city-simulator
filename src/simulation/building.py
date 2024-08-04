# src/simulation/building.py

class Building:
    """
    Class representing a building in the urban simulation.

    Attributes:
        id (int): The unique identifier of the building.
        coordinates_boundaries (list of tuples): A list of tuples containing the coordinates and the elevation
            of the boundaries of the building. The reference point of the boundary is the coordinates_location tuple
        coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
            of the building.
        num_floors (int): The number of floors in the building.
        floor_height (list of floats): A list containing the height of each floor in the building.
    """
    def __init__(self, id, coordinates_boundaries, coordinates_location, num_floors, floor_height):
        """
        Create a new instance of Building.
        Args:
            id (int): The unique identifier of the building.
            coordinates_boundaries (list of tuples): A list of tuples containing the coordinates and the elevation
                of the boundaries of the building. The reference point of the boundary is the coordinates_location tuple
            coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
                of the building.
            num_floors (int): The number of floors in the building.
            floor_height (list of floats): A list containing the height of each floor in the building.
        """
        self.id = id
        self.coordinates_boundaries = coordinates_boundaries
        self.coordinates_location = coordinates_location
        self.num_floors = num_floors
        self.floor_height = floor_height

class ResidentialBuilding(Building):
    """
    Class representing a residential building in the urban simulation.

    Attributes:
        id (int): The unique identifier of the building.
        coordinates_boundaries (list of tuples): A list of tuples containing the coordinates and the elevation
            of the boundaries of the building.
        coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
            of the building.
        num_units (int): The number of residential units in the building.
    """
    def __init__(self, id, coordinates_boundaries, coordinates_location, num_floors, floor_height, num_units):
        """
        Create a new instance of ResidentialBuilding.
        Args:
            id (int): The unique identifier of the building.
            coordinates_boundaries (list of tuples): A list of tuples containing the coordinates and the elevation
                of the boundaries of the building.
            coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
                of the building.
            num_floors (int): The number of floors in the building.
            floor_height (list of floats): A list containing the height of each floor in the building.
            num_units (int): The number of residential units in the building.
        """
        super().__init__(id, coordinates_boundaries, coordinates_location, num_floors, floor_height)
        self.num_units = num_units

class House(Building):
    """
    Class representing a house in the urban simulation.

    Attributes:
        id (int): The unique identifier of the building.
        coordinates_boundaries (list of tuples): A list of tuples containing the coordinates and the elevation
            of the boundaries of the building.
        coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
            of the building.
        num_floors (int): The number of floors in the house.
    """
    def __init__(self, id, coordinates_boundaries, coordinates_location, num_floors, floor_height):
        """
        Create a new instance of House.
        Args:
            id (int): The unique identifier of the building.
            coordinates_boundaries (list of tuples): A list of tuples containing the coordinates and the elevation
                of the boundaries of the building.
            coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
                of the building.
            num_floors (int): The number of floors in the house.
            floor_height (list of floats): A list containing the height of each floor in the house.
        """
        super().__init__(id, coordinates_boundaries, coordinates_location, num_floors, floor_height)

class WorkingBuilding(Building):
    """
    Class representing a working building in the urban simulation.

    Attributes:
        id (int): The unique identifier of the building.
        coordinates_boundaries (list of tuples): A list of tuples containing the coordinates and the elevation
            of the boundaries of the building.
        coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
            of the building.
        num_floors (int): The number of floors in the building.
        floor_height (list of floats): A list containing the height of each floor in the building. The first floor
            can have a different height.
        num_offices (int): The number of offices in the building.
    """
    def __init__(self, id, coordinates_boundaries, coordinates_location, num_floors, floor_height, num_offices):
        """
        Create a new instance of WorkingBuilding.
        Args:
            id (int): The unique identifier of the building.
            coordinates_boundaries (list of tuples): A list of tuples containing the coordinates and the elevation
                of the boundaries of the building.
            coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
                of the building.
            num_floors (int): The number of floors in the building.
            floor_height (list of floats): A list containing the height of each floor in the building. The first floor
                can have a different height.
            num_offices (int): The number of offices in the building.
        """
        super().__init__(id, coordinates_boundaries, coordinates_location, num_floors, floor_height)
        self.num_offices = num_offices

# Example usage:
residential_building = ResidentialBuilding(
    id=1,
    coordinates_boundaries=[((34.0522, -118.2437), 100), ((34.0523, -118.2438), 100)],
    coordinates_location=(34.0522, -118.2437),
    num_floors=5,
    floor_height=[3.0]*5,
    num_units=10
)

house = House(
    id=2,
    coordinates_boundaries=[((34.0522, -118.2437), 50), ((34.0523, -118.2438), 50)],
    coordinates_location=(34.0522, -118.2437),
    num_floors=2,
    floor_height=[2.5, 2.5]
)

working_building = WorkingBuilding(
    id=3,
    coordinates_boundaries=[((34.0522, -118.2437), 200), ((34.0523, -118.2438), 200)],
    coordinates_location=(34.0522, -118.2437),
    num_floors=10,
    floor_height=[4.0] + [3.0]*9,  # First floor is 4.0 meters, the rest are 3.0 meters
    num_offices=25
)


"""
Note for later:
    - Addition of a list of tuples with the coordinates of the building's polygon
    - Create inheritance with children classes : house, residential building, mall, working building ...
    - For now, we are handling coordinates in DD (decimal degrees) format, but we will incorporate a possible 
    switch to DMS (Degrees, Minutes, Seconds) format
"""