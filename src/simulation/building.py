# src/simulation/building.py

class Building:
    """
    Class representing a building in the urban simulation.

    Attributes:
        id (int): The unique identifier of the building.
        coordinates_boundaries (list): A list of tuples containing the coordinates and the elevation
            of the boundaries of the building. The reference point of the boundary is the coordinates_location tuple
        coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
            of the building.
    """
    def __init__(self, id, coordinates_boundaries, coordinates_location):
        """
        Create a new instance of City.
        Args:
            id (int): The unique identifier of the building.
            coordinates_boundaries (list): A list of tuples containing the coordinates and the elevation
                of the boundaries of the building. The reference point of the boundary is the coordinates_location tuple
            coordinates_location (tuple): A tuple containing the latitude and longitude of the bottom-left point
                of the building.
        """
        self.id = id
        self.coordinates_boundaries = coordinates_boundaries
        self.coordinates_location = coordinates_location




"""
Note for later:
    - Addition of a list of tuples with the coordinates of the building's polygon
    - Create inheritance with children classes : house, residential building, mall, working building ...
    - For now, we are handling coordinates in DD (decimal degrees) format, but we will incorporate a possible 
    switch to DMS (Degrees, Minutes, Seconds) format
"""