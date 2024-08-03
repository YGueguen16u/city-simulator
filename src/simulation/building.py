# src/simulation/building.py

class Building:
    """
    Class representing a building in the urban simulation.

    Attributes:
        id (int): The unique identifier of the building.
        coordinates_boundaries (list): A list of tuples containing the coordinates and the elevation
            of the boundaries of the building.
    """
    def __init__(self, id, coordinates_boundaries):
        """
        Create a new instance of City.
        Args:
            id (int): The unique identifier of the building.
            coordinates_boundaries (list): A list of tuples containing the coordinates and the elevation
                of the boundaries of the building.
        """
        self.id = id
        self.coordinates_boundaries = coordinates_boundaries


"""
Note for later:
    - Addition of a list of tuples with the coordinates of the building's polygon
    - Create inheritance with children classes : house, residential building, mall, working building ...
"""