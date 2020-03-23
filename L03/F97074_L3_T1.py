import sys

text = sys.argv[1].upper()
cypher = int(sys.argv[2]) % 26

start = ord("A")
end = ord("Z")

crypted = "".join([ chr(start + (((ord(t) - start) + cypher) % 26)) if (start <= ord(t) <= end) else t for t in text ])

print(crypted)
