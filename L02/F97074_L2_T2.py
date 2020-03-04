import sys

# get the words in lower case
words1 = sys.argv[1].lower()
words2 = sys.argv[2].lower()

# convert words2 to list of characters
words2 = [ char for char in words2 ]

# Go over the first words
# and remove it from the second
anagram = False

for char in words1:
    if char not in words2:
        anagram = False
        break
    words2.remove(char)

anagram = (len(words2) == 0)
print(anagram)
