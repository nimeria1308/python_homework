import argparse
import re
import sqlite3

DEFAULT_INPUT = "retn5_dat.txt"
DEFAULT_OUTPUT = "f97074-food.db"

# alas, the contents of the file do not match
# the description in the 2017 PDF, e.g.,
# non-text fields are also enclosed with ~

# ~0001~^~CHEESE,BAKED~^~303~^~Iron, Fe~^~100~^~~^~~
# code, descript, nmbr, nutname, retention
PATTERN = re.compile(r'.*~%s~\^~%s~\^~%s~\^~%s~\^~%s~\^.*' % (
    r'(?P<code>\d+)',
    r'(?P<descript>.+)',
    r'(?P<nmbr>\d+)',
    r'(?P<nutname>.+)',
    r'(?P<retention>\d+)',
))

def insert_row(cursor, match):
    # code, descript, nmbr, nutname, retention
    code = int(match.group('code'))
    descript = match.group('descript')
    nmbr = int(match.group('nmbr'))
    nutname = match.group('nutname')
    retention = int(match.group('retention'))

    cursor.execute("""
        insert into food
        (code, descript, nmbr, nutname, retention)
        values (%d, '%s', %d, '%s', %d)""" % (
            code, descript, nmbr, nutname, retention
        ))

def parse_into_database(input_file, db):
    cursor = db.cursor()
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='food'")

        if len(cursor.fetchall()):
            # already parsed
            return

        # create the table
        cursor.execute("""create table food (
            code INT,
            descript TEXT,
            nmbr INT KEY,
            nutname TEXT,
            retention INT,
            PRIMARY KEY (code, nmbr)
        )""")

        # parse all lines
        for line in input_file:
            match = PATTERN.match(line)
            if match:
                # insert into table
                insert_row(cursor, match)

        db.commit()

    finally:
        cursor.close()


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

    with sqlite3.connect(args.output) as db:
        # step 1. parse into the database
        parse_into_database(args.input, db)

        # step 2. execute query on db and display first result
        cursor = db.execute(args.query)
        try:
            row = cursor.fetchone()
            print(row)
        finally:
            cursor.close()

if __name__ == '__main__':
    main()

