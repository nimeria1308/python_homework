import sys

# get only the passed parameters
elements = sys.argv[1:]

# New list of unique elements
unique_elements = [ ]

for e in elements:
    if e not in unique_elements:
        unique_elements.append(e)

print(unique_elements)
