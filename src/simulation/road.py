# src/simulation/city.py
import xml.etree.ElementTree as ET
from xml.dom import minidom
import datetime


class Road:
    """
    Class representing a road in the urban simulation.

    Attributes:
        id (int): The unique identifier of the road.
        name (str): The name of the road.
        source (tuple): The coordinates of the starting node (latitude, longitude).
        target (tuple): The coordinates of the ending node (latitude, longitude).
        length (float): The length of the road.
        maxspeed (int): The maximum speed allowed on the road.
        oneway (bool): Indicates if the road is one-way.
        geometry (str): The geometry of the road as a LINESTRING.
    """

    def __init__(self, id, name, source, target, length, maxspeed, oneway, geometry):
        self.id = id
        self.name = name
        self.source = source
        self.target = target
        self.length = length
        self.maxspeed = maxspeed
        self.oneway = oneway
        self.geometry = geometry

    @staticmethod
    def generate_graphml(roads, filename):
        """
        Generate a GraphML file with the provided roads.

        Args:
            roads (list of Road): List of Road instances.
            filename (str): The name of the file to write the GraphML data.
        """
        graphml = ET.Element("graphml",
                             xmlns="http://graphml.graphdrawing.org/xmlns",
                             xmlns_xsi="http://www.w3.org/2001/XMLSchema-instance",
                             xsi_schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd")

        keys = [
            {"id": "d15", "for": "edge", "name": "geometry", "type": "string"},
            {"id": "d14", "for": "edge", "name": "length", "type": "string"},
            {"id": "d13", "for": "edge", "name": "reversed", "type": "string"},
            {"id": "d12", "for": "edge", "name": "oneway", "type": "string"},
            {"id": "d11", "for": "edge", "name": "maxspeed", "type": "string"},
            {"id": "d10", "for": "edge", "name": "highway", "type": "string"},
            {"id": "d9", "for": "edge", "name": "name", "type": "string"},
            {"id": "d8", "for": "edge", "name": "osmid", "type": "string"},
            {"id": "d7", "for": "node", "name": "street_count", "type": "string"},
            {"id": "d6", "for": "node", "name": "highway", "type": "string"},
            {"id": "d5", "for": "node", "name": "y", "type": "string"},
            {"id": "d4", "for": "node", "name": "x", "type": "string"},
            {"id": "d3", "for": "graph", "name": "simplified", "type": "string"},
            {"id": "d2", "for": "graph", "name": "crs", "type": "string"},
            {"id": "d1", "for": "graph", "name": "created_with", "type": "string"},
            {"id": "d0", "for": "graph", "name": "created_date", "type": "string"},
        ]

        for key in keys:
            ET.SubElement(graphml, "key", id=key["id"],
                          **{"for": key["for"], "attr.name": key["name"], "attr.type": key["type"]})

        graph = ET.SubElement(graphml, "graph", edgedefault="directed")
        ET.SubElement(graph, "data", key="d0").text = datetime.date.today().strftime('%Y-%m-%d')
        ET.SubElement(graph, "data", key="d1").text = "Custom Script"
        ET.SubElement(graph, "data", key="d2").text = "epsg:4326"
        ET.SubElement(graph, "data", key="d3").text = "True"

        node_id_map = {}
        node_counter = 1

        def add_node(coord):
            nonlocal node_counter
            if coord not in node_id_map:
                node_id_map[coord] = node_counter
                node = ET.SubElement(graph, "node", id=str(node_counter))
                ET.SubElement(node, "data", key="d4").text = str(coord[1])  # Longitude
                ET.SubElement(node, "data", key="d5").text = str(coord[0])  # Latitude
                node_counter += 1
            return node_id_map[coord]

        for road in roads:
            source_id = add_node(road.source)
            target_id = add_node(road.target)
            edge = ET.SubElement(graph, "edge", source=str(source_id), target=str(target_id))
            ET.SubElement(edge, "data", key="d8").text = str(road.id)
            ET.SubElement(edge, "data", key="d9").text = road.name
            ET.SubElement(edge, "data", key="d10").text = "residential"  # Placeholder, replace with actual type
            ET.SubElement(edge, "data", key="d11").text = str(road.maxspeed)
            ET.SubElement(edge, "data", key="d12").text = str(road.oneway)
            ET.SubElement(edge, "data", key="d13").text = "False"
            ET.SubElement(edge, "data", key="d14").text = str(road.length)
            ET.SubElement(edge, "data", key="d15").text = road.geometry

        tree = ET.ElementTree(graphml)
        with open(filename, "wb") as f:
            tree.write(f, encoding="utf-8", xml_declaration=True)

        # Beautify the XML
        with open(filename, "r") as f:
            xml_string = f.read()

        dom = minidom.parseString(xml_string)
        pretty_xml_as_string = dom.toprettyxml()

        with open(filename, "w") as f:
            f.write(pretty_xml_as_string)

    def __str__(self):
        return f'Road {self.id}: {self.name} from {self.source} to {self.target}, {self.length}m, maxspeed: {self.maxspeed}km/h, oneway: {self.oneway}'
