from F97074_L8_T1 import Fibs

fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

print(list(Fibs(12)))
