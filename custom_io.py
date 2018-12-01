def read_lines(name):
    with open(name) as fh:
        return fh.read().splitlines()
