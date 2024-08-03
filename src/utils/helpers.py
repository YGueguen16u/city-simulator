# src/utils/helpers.py

import math


def dms_to_dd(coordinates):
    """
    Converts coordinates in DMS format to DD format
    Args :
        coordinates (list): list of coordinates in DMS format.
    Return:
        coordinates (list): list of coordinates in DD format.
    """
    pass


def dd_to_dms(coordinates):
    """
    Converts coordinates in DD format to DMS format
    Args :
        coordinates (list): list of coordinates in DD format.
    Return:
        coordinates (list): list of coordinates in DMS format.
    """
    pass


def haversine_distance(coord1, coord2):
    """
    Calculate the great-circle distance between two points on the Earth surface using the Haversine formula.

    Args:
        coord1 (tuple): A tuple representing the latitude and longitude of the first point in decimal degrees.
        coord2 (tuple): A tuple representing the latitude and longitude of the second point in decimal degrees.

    Returns:
        float: The distance between the two points in meters.
    """
    R = 6371000  # Radius of the Earth in meters

    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))

    distance = R * c
    return distance