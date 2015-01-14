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
            
    def bin_search(self, item, lst, low, high):
#==============================================================================
#       Binary search
#         IN: int, item to be found
#             list, list of items to be searched
#         OUT: index of item or -1 if item not found
#==============================================================================
        if low > high:
            print 'not found'
            return -1
        midpoint = (low + high)/2
        if lst[midpoint] == item:
            print 'found ', midpoint
            return midpoint
        if lst[midpoint] > item:
            self.bin_search(item, lst, low, midpoint)
        elif lst[midpoint] < item:
            self.bin_search(item, lst, midpoint+1, high)            


if __name__ == '__main__':
    alg = Algorithms()
    item = 2
    lst = [0, 1, 2, 3, 4]
    print alg.bin_search(item, lst, 0, len(lst) -1)
