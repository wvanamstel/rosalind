'''
Created on Jun 24, 2014

@author: w
'''

def main():
    print dna_motif('rosalind_subs.txt')

def dna_motif(file_name):
    with open(file_name) as fin:
        content = fin.read().splitlines()
    fin.close()

    dna_string = content[0]
    sub_string = content[1]
    
    i = 0
    positions = ""
    while i < len(dna_string):
        if (dna_string.find(sub_string, i) != -1):
            sub_string_pos =  dna_string.find(sub_string, i) + 1
            i = sub_string_pos
            positions += str(sub_string_pos) + ' '
        i+=1
        
    return positions
    
def rna_to_protein(file_name):
    import re
    fin = open(file_name, 'r')
    content = fin.read()
    fin.close()
    codons = re.findall(r'.{1,3}', content, re.DOTALL) #split 3 letter codons from string
    
    fin = open('codon_table.txt', 'r') #load codon table and put in dict
    codon_list = fin.read().split()
    fin.close()
    codon_table = {}
    i = 0
    while i < len(codon_list):
        codon_table[ codon_list[i] ] = codon_list[i + 1]
        i += 2
        
    protein_string = '' #construct protein string using codons and codon table
    for codon in codons:
        if(codon_table[codon] == 'Stop'):
            break
        protein_string += codon_table[codon]
        
    return protein_string
    
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