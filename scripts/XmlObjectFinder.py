import xml.etree.ElementTree as ET

class XmlObjectFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = ET.parse(file_path)
        
    def find_objects_by_name(self, name):
        result = []
        if not len(name):
            return self.tree.getroot().findall('object')
        else:
            for obj in self.tree.getroot().findall('object'):
                if obj.find('name').text == name:
                    result.append(obj)
        return result



if __name__ == "__main__":
    print("CASE 1: XML is empty")
    path_to_xml = 'scripts/test_data/empty.xml'
    try:
        xml_parser = XmlObjectFinder(path_to_xml)
        print("TEST NOT PASSED")
    except Exception:
        print("TEST PASSED")
        
    print("CASE 2: XML with data but no objects on it")
    path_to_xml = 'scripts/test_data/0_objects.xml'
    xml_parser = XmlObjectFinder(path_to_xml)
    if len(xml_parser.find_objects_by_name("fish")) == 0:
        print("TEST PASSED")
    else:
        print("TEST NOT PASSED")

    print("CASE 3: XML with data and one object on it")
    path_to_xml = 'scripts/test_data/1_object.xml'
    xml_parser = XmlObjectFinder(path_to_xml)
    if len(xml_parser.find_objects_by_name("fish")) == 1:
        print("TEST PASSED")
    else:
        print("TEST NOT PASSED")
    
    print("CASE 4: XML with data and two object on it")
    path_to_xml = 'scripts/test_data/2_objects.xml'
    xml_parser = XmlObjectFinder(path_to_xml)
    if len(xml_parser.find_objects_by_name("fish")) == 2:
        print("TEST PASSED")
    else:
        print("TEST NOT PASSED")

    print("CASE 5: XML with data and two different objects on it")
    path_to_xml = 'scripts/test_data/2_objects_different_classes.xml'
    xml_parser = XmlObjectFinder(path_to_xml)
    if len(xml_parser.find_objects_by_name("fish")) == 1 and len(xml_parser.find_objects_by_name("fish2")) == 1 and len(xml_parser.find_objects_by_name("")) == 2:
        print("TEST PASSED")
    else:
        print("TEST NOT PASSED")
    