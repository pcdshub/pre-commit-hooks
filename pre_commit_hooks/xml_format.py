#!C:/miniconda/envs/plc-pre-commit/python.exe

import argparse

from lxml import etree

TAB_WIDTH = 2
RETRIES = 5


def fix_file(
    filename: str,
    tab_width: int = TAB_WIDTH,
    retries: int = RETRIES,
) -> None:
    """
    Read a file, fix it, write the fix back to the file handle
    """
    # lxml throws encoding errors unless we work in binary mode
    with open(filename, "rb") as fd:
        original_xml = fd.read()
    iter_xml = original_xml

    for _ in range(retries):
        new_xml = xml_once(
            original_xml=iter_xml,
            tab_width=tab_width,
        )
        if new_xml == iter_xml:
            break
        iter_xml = new_xml

    if new_xml != original_xml:
        print(f"Fixing {filename}")
        with open(filename, "wb") as fd:
            fd.write(new_xml)


def xml_once(original_xml: str, tab_width: int) -> str:
    """
    One iteration of the xml formatting.

    This may need to run several times due to inconsistencies in lxml.
    """
    # lxml is the easiest cross-platform way to do this using pre-commit
    # xmllint is cross-platform but pre-commit does not help us set it up
    xml_parser = etree.XMLParser(remove_blank_text=True)
    parse_tree = etree.XML(original_xml, parser=xml_parser).getroottree()
    etree.indent(parse_tree, space=" " * tab_width)
    new_xml = etree.tostring(parse_tree,
                             pretty_print=True,
                             xml_declaration=True,
                             encoding=parse_tree.docinfo.encoding)

    # lxml does not preserve line endings, so we must do it ourselves.
    # lxml always outputs with unix line endings (LF)
    if b'\r\n' in original_xml:
        new_xml = new_xml.replace(b'\n', b'\r\n')
    return new_xml


def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser()
        parser.add_argument("filenames", nargs="*")
        parser.add_argument("--tab-width", type=int, default=TAB_WIDTH)
        parser.add_argument("--retries", type=int, default=RETRIES)
        args = parser.parse_args()
    try:
        for filename in args.filenames:
            fix_file(filename, tab_width=args.tab_width)
        return 0
    except Exception as exc:
        print(exc)
        return 1


if __name__ == '__main__':
    exit(main())
