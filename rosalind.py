'''
Created on Jun 24, 2014

@author: w
'''

def main():
    permutations(7)

def permutations(i):
    import itertools
    import math
    
    j= range(1,i + 1)
    
    print math.factorial(i)
    for item in list(itertools.permutations(j, i)):
        solution = ""
        for element in item:
            solution += str(element)
            solution += " "
        print solution
    
    

def first_mendel(k, m, n):
    total = k + m + n
    
    prob1 = ( (k/total) * (k-1/(total-1)) ) + ( (k/total) * (m/(total-1)) ) * 2
    prob2 = ( (n/total) * (k/(total-1)) ) +   ( (n/total) * (m/(total-1))*0.5 )
    prob3 = ( (m/total) * 0.5 * (n/(total-1)) ) + ( (m/total) * 0.5 + (k/(total-1)) )
    
    prob = prob1 + prob2 + prob3  
    return prob

if __name__ == '__main__':
    main()