import itertools
import os
import sys

from math import copysign

# https://en.wikipedia.org/wiki/Bisection_method
#
# INPUT: Function f,
#        endpoint values a, b,
#        tolerance TOL,
#        maximum iterations NMAX
# CONDITIONS: a < b,
#             either f(a) < 0 and f(b) > 0 or f(a) > 0 and f(b) < 0
# OUTPUT: value which differs from a root of f(x) == 0 by less than TOL

def bisection(a, b, f, tolerance=0.001, max_iter=None):
    # parvonachalni proverki
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("a and b need to be numbers")

    # podrejdame gi taka, che a < b (ima go v usloviata)
    a, b = sorted((a, b))

    f_a = f(a)
    f_b = f(b)

    if not ((f_a < 0 and f_b > 0) or (f_a > 0 and f_b < 0)):
        raise ValueError("f(x) has not roots in [%f, %f]: f(a) = %f and f(b) = %f have the same signs" % (a, b, f_a, f_b))

    # implementation

    # N = 1
    # while N ≤ NMAX do // limit iterations to prevent infinite loop
    #     c = (a + b)/2 // new midpoint
    #     if f(c) == 0 or (b – a)/2 < TOL then // solution found
    #         Output(c)
    #         Stop
    #     end if
    #     N = N + 1 // increment step counter
    #     if sign(f(c)) = sign(f(a)) then a = c else b = c // new interval
    # end while
    # Output("Method failed.") // max number of steps exceeded

    # ako max_iter e podadeno, polzvame range(), za da ogranichim broq
    # na iteraciite, inache polzvame itertools.count(), za da broim
    # do bezkrainost
    for _ in range(max_iter) if max_iter else itertools.count():
        c = (a + b) / 2 # new midpoint
        f_c = f(c)
        if (f_c == 0) or (((b - a) / 2) < tolerance):
            # solution found
            return c

        # new interval
        if copysign(1.0, f_c) == copysign(1.0, f(a)):
            a = c
        else:
            b = c

    raise ValueError("Reached maximum number of iterations, but did not find a good enough root")

def main():
    import math

    def f_1(x):
        return x*x*x + 3*x - 5

    def f_2(x):
        return math.exp(x) - 2*x -2

    functions = [
        (f_1, "x*x*x + 3*x - 5" ),
        (f_2, "exp(x) - 2*x -2" ),
    ]

    fn_index = 0

    if len(sys.argv) > 1:
        fn_index = int(sys.argv[1]) % len(functions)

    fn = functions[fn_index]

    print("Available functions:")
    for idx, f in enumerate(functions):
        print("  function[%d]: %s" % (idx, f[1]))
    print()

    print("Using function %d. To use another function, pass it as an argument, e.g.:" % fn_index)
    print("  $ %s 1" % os.path.basename(sys.argv[0]))
    print()

    my_input = input

    # check if in Python 2
    try:
        my_input = raw_input
    except NameError: pass

    while True:
        try:
            print("Looking for roots for `%s`." % fn[1])
            a = my_input("Please, enter start of search interval [a: ")
            b = my_input("Please, enter end of search interval b]: ")
            r = bisection(a, b, fn[0])
            print("Found root %f" % r)

        except Exception as e:
            print("Error: %s" % e)

        print()

if __name__ == '__main__':
    main()
