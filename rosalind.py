'''
Created on Jun 24, 2014

@author: w
'''

def main():
    print first_mendel(21.,28.,28.)



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
    '''calculate probability that from 3 gene pairs DD Dd dd, there will be offspring
    with a dominant allele'''
    total = (k + m + n)*2 #total number of alleles
    num_dom = k*2 + m #number of dominant
    num_rec = m + n*2 #number of recessive
    
    #probability of an offspring with >=1 dominant allele
    prob1 = (num_dom/total) * (num_dom-1)/(total-1) + ( (num_dom/total) * (num_rec/(total-1)) ) + ( (num_rec/total) * (num_dom/(total-1)) )
    #prob2 = (num_rec/total)*((num_rec-1)/(total-1)) #complement
    
    return prob1

if __name__ == '__main__':
    main()