import sys

# get only the passed parameters
elements = sys.argv[1:]

# copy and sort the list
sorted_elements = elements[:]
sorted_elements.sort()

if elements == sorted_elements:
    print("sorted")
else:
    print("not sorted")
