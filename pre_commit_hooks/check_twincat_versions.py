import xml.etree.ElementTree as ET
from importlib.abc import Traversable
from typing import Union


def tc_version_pinned(filename: Union[Traversable, str]) -> bool:
    tree = ET.parse(filename)
    root = tree.getroot()

    return 'TcVersionFixed' in root.attrib


def get_tc_version(filename: Union[Traversable, str]) -> str:
    tree = ET.parse(filename)
    root = tree.getroot()

    return root.attrib.get('TcVersion')
