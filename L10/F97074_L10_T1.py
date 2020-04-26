import os
import sys

def sort_file_lines(input_filename, output_filename):
    # read file into lines
    with open(input_filename, 'r') as f:
        lines = f.readlines()

    # sort inplace
    lines.sort()

    # write lines into file
    with open(output_filename, "w") as f:
        f.writelines(lines)

def usage():
    print("A simple app that sortes the lines in a file")
    print("Usage:")
    print("  $ %s <input> <output>" % os.path.basename(sys.argv[0]))
    print()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Please, specify input and ouput filenames")
        print()
        usage()
        exit(1)

    sort_file_lines(sys.argv[1], sys.argv[2])
