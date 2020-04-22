import math
import unittest

from F97074_L9_T1 import bisection

def f_no_roots(x):
    return x * x

def f_trivial(x):
    return x

# vmesto explicitno da pisha keisove i suites
# shte se vuzpolzvame ot implicitnite imena i tipove
class MyTestCases(unittest.TestCase):

    # testvame s argumenti, koito ne sa chisla
    def test_arguments_non_numbers(self):
        self.assertRaises(TypeError, bisection, "x", 2, f_trivial)
        self.assertRaises(TypeError, bisection, 2, "x", f_trivial)

    # testvame dali priema i int, i float
    def test_arguments_numbers(self):
        bisection(-2, 3.14, f_trivial)

    # testvame dali raise-va, kogato funkciata nqma koreni
    def test_f_no_roots(self):
        self.assertRaises(ValueError, bisection, 1, 2, f_no_roots)

    # proverqvame funkcionalnostta za limitirane na iteraciite
    def test_iterations(self):
        self.assertRaises(ValueError, bisection, -1, 2, math.sin, 0.000001, 10)

    # helper
    def check_roots(self, data, tolerance=0.001):
        for f, roots in data:
            for a, b, x in roots:
                result = bisection(a, b, f, tolerance)
                difference = abs(x - result)
                self.assertLess(difference, tolerance)

    def test_roots(self):
        def f_1(x):
            return x*x*x + 3*x - 5

        def f_2(x):
            return math.exp(x) - 2*x -2

        data = [
            (f_1,
                [
                    (-10, 10, 1.1542 ),
                ]
            ),
            (f_2,
                [
                    (-10, 0, -0.768039),
                    (0, 10, 1.678835),
                ]
            ),
        ]


        self.check_roots(data)

if __name__ == '__main__':
    unittest.main()
