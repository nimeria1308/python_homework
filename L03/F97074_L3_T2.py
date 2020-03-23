import sys

text = sys.argv[1].upper()
cypher = sys.argv[2].upper()

start = ord("A")
end = ord("Z")

crypted = [ ]
for x in range(len(text)):
    t = text[x]
    if start <= ord(t) <= end:
        c = ord(cypher[x % len(cypher)])
        t = chr(start + ((ord(t) + c) % 26))
    crypted.append(t)

crypted = "".join(crypted)
print(crypted)
