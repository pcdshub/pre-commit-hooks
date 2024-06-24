import re
import xml.etree.ElementTree as ET


def tc_version_pinned(xml_content: str) -> bool:
    root = ET.fromstring(xml_content)

    return 'TcVersionFixed' in root.attrib and root.attrib.get('TcVersionFixed') == 'true'


def get_tc_version(xml_content: str) -> str:
    root = ET.fromstring(xml_content)

    return root.attrib.get('TcVersion')


def fix_tc_version(xml_content: str, new_version: str) -> str:
    pattern = r'(TcVersion=")([^"]*)(")'
    new_xml_content = re.sub(pattern, r'\g<1>' + new_version + r'\g<3>', xml_content)

    return new_xml_content


def fix_pinned_version(xml_content: str, pin_version: bool) -> str:
    new_value = 'true' if pin_version else 'false'

    pattern = r'(TcVersionFixed=")([^"]*)(")'

    if re.search(pattern, xml_content):
        new_xml_content = re.sub(pattern, r'\g<1>' + new_value + r'\g<3>', xml_content)
    else:
        version_pattern = r'(TcVersion="[^"]*")'
        new_xml_content = re.sub(version_pattern, r'\g<1> TcVersionFixed="' + new_value + r'"', xml_content)

    return new_xml_content
