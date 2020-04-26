import os
import sys

def read_stems_from_file(input_filename):
    stems = { }

    # read file line by line into the dictionary
    with open(input_filename, 'r') as f:
        for line in f:
            # split
            pair = line.split(':')

            # check if the line is OK
            if len(pair) != 2:
                continue

            # unpack
            key, value = pair

            # stuff it into the dict
            stems[key.strip().lower()] = value.strip().lower()
    
    return stems

def usage():
    print("A simple app that reads a stem dictionary from a file and returns a stem for a given word")
    print("Usage:")
    print("  $ %s <input> <word>" % os.path.basename(sys.argv[0]))
    print()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please, specify input stem filename and a word to look up")
        print()
        usage()
        exit(1)

    stems = read_stems_from_file(sys.argv[1])
    word = sys.argv[2].lower()

    if word not in stems and word not in stems.values():
        print("Unknown word %s" % word)
        exit(1)

    # now look for it recursively
    # for example:
    # * notaword -> notaword
    # * better -> well
    # * quelier -> quietly -> quiet (not currently available in the stemA.txt, but this script would support it)
    # note: if there is a cycle in the dictionary, it will hang
    while word in stems:
        word = stems[word]

    print(word)
