import argparse
import re

MAX_REPLACE = 10
TAB_WIDTH = 4


def fix_file(filename, tab_width=TAB_WIDTH, max_replace=MAX_REPLACE):
    with open(filename, 'r') as fd:
        original_lines = fd.readlines()
    new_lines = []
    regex = re.compile(r'^\s*\t')
    for line in original_lines:
        replace_count = 0
        while regex.match(line) and replace_count < MAX_REPLACE:
            replace_count += 1
            line.replace('\t', ' ' * tab_width, 1)
        if not replace_count < MAX_REPLACE:
            raise RuntimeError('Reached max tab replacements for one line '
                               f'({max_replace}). Aborting to avoid '
                               'infinite loop.')
        new_lines.append(line)
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
