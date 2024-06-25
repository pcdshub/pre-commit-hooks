import argparse

from lxml import etree


def structured_text_formatter(path: str, lines: int = 1) -> None:
    root = etree.parse(path).getroot()
    sect = root.xpath(".//Declaration|.//Implementation/ST")
    if len(sect) == 0:
        return

    newlines = "\n" * lines
    for section in sect:
        try:
            section.text = etree.CDATA(newlines + section.text.strip("\n") + newlines)
        except AttributeError:
            pass
    etree.ElementTree(root).write(path, encoding="utf-8", xml_declaration=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lines", type=int, default=1)
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    try:
        for file in args.files:
            structured_text_formatter(file, args.lines)
    except:
        return 1


if __name__ == "__main__":
    exit(main())
