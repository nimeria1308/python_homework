class Fibs(object):
    def __init__(self, n=None):
        self.n = n

    def __iter__(self):
        class It(object):
            def __init__(self, max):
                self.n = -1
                self.a = 0
                self.b = 1
                self.max = max

            def __next__(self):
                self.n += 1

                if self.max is not None and self.n > self.max:
                    raise StopIteration

                if self.n == 0:
                    return 0
                elif self.n == 1:
                    return 1
                else:
                    sum = self.a + self.b
                    self.a = self.b
                    self.b = sum
                    return sum

        return It(self.n)
