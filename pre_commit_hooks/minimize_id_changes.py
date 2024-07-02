import argparse
import xml.etree.ElementTree as ET
from importlib.abc import Traversable
from typing import Union

from pre_commit_hooks.exceptions import PreCommitException


def minimize_id_changes_checked(filename: Union[Traversable, str]) -> None:
    tree = ET.parse(filename)
    root = tree.getroot()

    combine_ids_element = root.find(".//{*}CombineIds")

    if combine_ids_element is None or combine_ids_element.text.lower() == "false":
        raise PreCommitException(
            f"Minimize id changes not checked in {filename}. "
            f"To enable this go to Project settings > Common and select 'Minimize Id changes in TwinCAT files.'"
        )


def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser()
        parser.add_argument("filenames", nargs="*")
        args = parser.parse_args()
    try:
        for filename in args.filenames:
            minimize_id_changes_checked(filename)
        return 0
    except Exception as exc:
        print(exc)
        return 1


if __name__ == "__main__":
    exit(main())
