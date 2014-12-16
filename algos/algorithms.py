import numpy as np


class Algorithms(object):

    def __init__(self):
        pass

    def fibo(self, n=100):
        # fibonacci series, generates first 100 or user defined number
        x, y = 1, 1
        for _ in xrange(n):
            yield x
            x, y = y, x + y

if __name__ == '__main__':
    alg = Algorithms()
    for i in alg.fibo(10):
        print i
