import argparse
import sqlite3

DEFAULT_INPUT = "retn5_dat.txt"
DEFAULT_OUTPUT = "retn5_dat.sqlite"


def main():
    parser = argparse.ArgumentParser(
        description="Parses USDA txt file into SQLite3 DB and executes a query on it.")

    parser.add_argument('query',
            help='SQL query to execute on the data')
 
    parser.add_argument('--input', '-i',
            help='input file to parse (default %s)' % DEFAULT_INPUT,
            default=DEFAULT_INPUT, type=argparse.FileType('r'))
    parser.add_argument('--output', '-o',
            help='output sqlite file (default %s)' % DEFAULT_OUTPUT,
            default=DEFAULT_OUTPUT)

    args = parser.parse_args()

    print(args)

if __name__ == '__main__':
    main()

