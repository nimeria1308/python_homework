import sys

# get only the passed parameters
elements = sys.argv[1:]

# Check if the count of any of its elements is > 1
repeats = False
for e in elements:
    if elements.count(e) > 1:
        repeats = True
        break

print(repeats)
