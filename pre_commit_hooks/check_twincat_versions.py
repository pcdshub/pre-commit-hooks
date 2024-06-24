import argparse
import re
import xml.etree.ElementTree as ET
from pre_commit_hooks.exceptions import PreCommitException


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


def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser()
        parser.add_argument('filenames', nargs='+', help='List of XML filenames to process')
        parser.add_argument('--target-version', type=str, help='Target TcVersion to enforce')
        parser.add_argument('--fix', action='store_true', help='Fix the versions if they do not match the target version')
        parser.add_argument('--reason', type=str, help='Reason for pinning the version')
        args = parser.parse_args()

    try:
        versions = {}
        for filename in args.filenames:
            with open(filename, 'r') as file:
                xml_content = file.read()
                version = get_tc_version(xml_content)
                versions[filename] = version

        itemize = "\n -"
        if args.target_version:
            mismatched_files = [fname for fname, ver in versions.items() if ver != args.target_version]
            if mismatched_files:
                if args.fix:
                    for filename in mismatched_files:
                        with open(filename, 'r') as file:
                            xml_content = file.read()
                        fixed_content = fix_tc_version(xml_content, args.target_version)
                        with open(filename, 'w') as file:
                            file.write(fixed_content)
                    print(f"Fixed TwinCAT versions for:{itemize}{itemize.join(mismatched_files)}")
                else:
                    reason_msg = f"\nReason: {args.reason}" if args.reason else ""
                    raise PreCommitException(
                        "The following files are not set to the targeted TwinCAT version "
                        f"{args.target_version}:{itemize}{itemize.join(mismatched_files)}{reason_msg}")
        else:
            unique_versions = set(versions.values())
            if len(unique_versions) > 1:
                raise PreCommitException(
                    "Not all files have the same TwinCAT version:"
                    f"{itemize}" + itemize.join(f"{fname}: {ver}" for fname, ver in versions.items()))

        return 0
    except Exception as exc:
        print(exc)
        return 1


if __name__ == "__main__":
    exit(main())
