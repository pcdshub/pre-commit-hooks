import argparse
import re

TAB_WIDTH = 4


def fix_file(filename, tab_width=TAB_WIDTH):
    with open(filename, 'r') as fd:
        original_lines = fd.readlines()
    new_lines = []
    changed = False
    # Match all leading whitespace and group it
    regex = re.compile(r'^(\s+)')
    for line in original_lines:
        match = regex.match(line)
        if match:
            leading_whitespace = match.groups()[0]
            # Fix if leading whitespace contain tabs
            if '\t' in leading_whitespace:
                changed = True
                line = (leading_whitespace.replace('\t', ' ' * tab_width)
                        + line.lstrip())
        new_lines.append(line)
    if changed:
        print(f'Fixing {filename}')
        with open(filename, 'w') as fd:
            fd.write(''.join(new_lines))


def main(args=None):
    if args is None:
        parser = argparse.ArgumentParser()
        parser.add_argument('filenames', nargs='*')
        args = parser.parse_args()
    try:
        for filename in args.filenames:
            fix_file(filename)
        return 0
    except Exception as exc:
        print(exc)
        return 1


if __name__ == "__main__":
    exit(main())
