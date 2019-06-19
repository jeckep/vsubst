import argparse
import os

DELIM = '='


def replace_in_files(src, dst, replaces):
    if os.path.isfile(src):
        replace_in_file(src, dst, replaces)
    else:
        for root, dirs, files in os.walk(src):
            for fname in files:
                full_src_path = os.path.join(root, fname)
                relpath = os.path.relpath(full_src_path, src)
                full_dst_path = os.path.join(dst, relpath)
                replace_in_file(full_src_path, full_dst_path, replaces)


def replace_in_file(full_src_path, full_dst_path, replaces):
    with open(full_src_path) as f:
        data = f.read()

    for _from, _to in replaces.items():
        data = data.replace('${' + _from + '}', _to)

    dirname, _ = os.path.split(full_dst_path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(full_dst_path, 'w') as f:
        f.write(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--props', help='props')
    parser.add_argument('--src_path', help='src_path')
    parser.add_argument('--dst_path', help='src_path')

    args = parser.parse_args()

    replaces = {}
    for line in open(args.props):
        if is_not_blank(line) and not line.strip().startswith("#"):
            src, dst = [s.strip() for s in line.split(DELIM)]
            replaces[src] = dst

    replace_in_files(args.src_path, args.dst_path, replaces)


def is_not_blank(line):
    return bool(line and line.strip())


if __name__ == '__main__':
    main()
