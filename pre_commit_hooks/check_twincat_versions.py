import re
import xml.etree.ElementTree as ET


def tc_version_pinned(xml_content: str) -> bool:
    root = ET.fromstring(xml_content)

    return 'TcVersionFixed' in root.attrib


def get_tc_version(xml_content: str) -> str:
    root = ET.fromstring(xml_content)

    return root.attrib.get('TcVersion')


def fix_tc_version(xml_content: str, new_version: str) -> str:
    pattern = r'(TcVersion=")([^"]*)(")'
    new_xml_content = re.sub(pattern, r'\g<1>' + new_version + r'\g<3>', xml_content)

    return new_xml_content
