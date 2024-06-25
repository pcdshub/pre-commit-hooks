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

    added_libraries = set(
        el.attrib["Include"] for el in parse_tree.iter("{*}PlaceholderReference")
    )
    fixed_version_libraries = set(
        el.attrib["Include"] for el in parse_tree.iter("{*}PlaceholderResolution")
    )

    non_fixed_library_versions = added_libraries - fixed_version_libraries

    if len(non_fixed_library_versions) == 1:
        raise PreCommitException(
            f"Library version of {list(non_fixed_library_versions)[0]} is not fixed!"
        )
    elif len(non_fixed_library_versions) > 1:
        raise PreCommitException(
            f"Library version of {', '.join(non_fixed_library_versions)} are not fixed!"
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
