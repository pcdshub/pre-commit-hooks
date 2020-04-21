import argparse
import subprocess


def fix_file(filename):
    output = subprocess.check_output(['xmllint', '--format', filename],
                                     universal_newlines=True)
    with open(filename, 'r') as fd:
        original_file = fd.read()
    if output != original_file:
        print(f'Fixing {filename}')
        with open(filename, 'w') as fd:
            fd.write(output)


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


if __name__ == '__main__':
    exit(main())
