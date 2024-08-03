import math

from geopy.distance import geodesic


def dms_to_dd(dms):
    """
    Converts coordinates in DMS format to DD format.
    Args:
        dms (tuple): tuple representing the coordinates in DMS format (degrees, minutes, seconds).
    Returns:
        float: The coordinates in DD format.
    """
    degrees, minutes, seconds = dms
    dd = degrees + minutes / 60 + seconds / 3600
    return dd


def dd_to_dms(dd):
    """
    Converts coordinates in DD format to DMS format.
    Args:
        dd (float): The coordinates in DD format.
    Returns:
        tuple: tuple representing the coordinates in DMS format (degrees, minutes, seconds).
    """
    degrees = int(dd)
    minutes = int((dd - degrees) * 60)
    seconds = (dd - degrees - minutes / 60) * 3600
    return degrees, minutes, seconds


# We give up haversine_distance because less accurate than geopy
def haversine_distance(coord1, coord2):
    """
    Calculate the great-circle distance between two points on the Earth surface using the Haversine formula.
    Args:
        coord1 (tuple): A tuple representing the latitude and longitude of the first point in decimal degrees.
        coord2 (tuple): A tuple representing the latitude and longitude of the second point in decimal degrees.
    Returns:
        float: The distance between the two points in meters.
    """
    R = 6378137  # Radius of the Earth in meters

    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    distance = R * c
    return distance


# Test coordinates
A = (45.75194444, 4.83305556)
B = (45.76166667, 4.83388889)
C = (45.76138889, 4.84777778)
D = (45.75250000, 4.84750000)

# Calculate distances using haversine formula
AB = haversine_distance(A, B) / 1000
BC = haversine_distance(B, C) / 1000
CD = haversine_distance(C, D) / 1000
DA = haversine_distance(A, D) / 1000

# Calculate distances using geopy
ABg = geodesic(A, B).kilometers
BCg = geodesic(B, C).kilometers
CDg = geodesic(C, D).kilometers
DAg = geodesic(A, D).kilometers

print(f"AB: {AB}, BC: {BC}, CD: {CD}, DA: {DA}")
print(f"ABg :{ABg}, BCg :{BCg}, CDg :{CDg}, DAg :{DAg} ")
print(f"differences : AB : {abs(AB-ABg)}, BC : {abs(BC-BCg)}, CD : {abs(CD-CD)}, DA : {abs(DA-DA)}")

"""
AB: 1.084207288824753, BC: 1.0790770397423044, CD: 0.9897418807246884, DA: 1.123669093021847
ABg :1.0825357569768936, BCg :1.0809328722294185, CDg :0.9882059817610646, DAg :1.1255928863879379 
differences : AB : 0.0016715318478592867, BC : 0.001855832487114073, CD : 0.0, DA : 0.0
"""