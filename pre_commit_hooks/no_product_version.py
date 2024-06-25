#!/usr/bin/env python

import argparse

from lxml import etree


class PreCommitException(Exception):
    pass


def check_file(filename):
    with open(filename, "rb") as fd:
        original_xml = fd.read()

    xml_parser = etree.XMLParser(remove_blank_text=True)
    parse_tree = etree.XML(original_xml, parser=xml_parser).getroottree()

    tc_plc_object = list(parse_tree.iter("TcPlcObject"))[0].attrib
    # Check if it contains a product version attribute
    if "ProductVersion" in tc_plc_object:
        raise PreCommitException(
            f"Detected product version ({tc_plc_object['ProductVersion']}) in {filename}. "
            f"To disable this go to Project settings > Advanced and disable 'Write product version in files.'"
        )


def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser()
        parser.add_argument("filenames", nargs="*")
        args = parser.parse_args()
    try:
        for filename in args.filenames:
            check_file(filename)
        return 0
    except Exception as exc:
        print(exc)
        return 1


if __name__ == "__main__":
    exit(main())
