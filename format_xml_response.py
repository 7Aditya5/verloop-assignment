import xml.etree.ElementTree as ET


def format_xml_response(data):
    declaration = '<?xml version="1.0" encoding="UTF-8"?>'
    root = ET.Element("root")
    temperature=ET.SubElement(root,"Temperature")
    temperature.text=str(data["current"]["temp_c"])
    city = ET.SubElement(root, "City")
    city.text = data["location"]["name"]
    lat = ET.SubElement(root, "Latitude")
    lat.text = str(data["location"]["lat"])
    lon = ET.SubElement(root, "Longitude")
    lon.text = str(data["location"]["lon"])
    xml_data = declaration+ET.tostring(root, encoding="utf-8", method="xml").decode()
    return xml_data