'''
Created on Jun 24, 2014

@author: w
'''

class Rosalind(object):
    def __init__(self):
        pass

    def cons(self, file_name):
        '''construct consensus list and profile matrix from a number
        of dna strings, input is FASTA style'''
        import numpy as np

        with open(file_name) as fin:
            content = fin.read().splitlines()
        fin.close()

        dna_length = len(content[1])

        profile = {'A': np.zeros((1,dna_length)), 'C': np.zeros((1,dna_length)), 'G': np.zeros((1,dna_length)), 'T': np.zeros((1, dna_length))}
        for line in content:
            if line[0] != '>':
                dna_string = list(line)
                for i in range(dna_length):
                    if line[i] == 'A':
                        profile['A'][0][i] += 1
                    elif line[i] == 'C':
                        profile['C'][0][i] += 1
                    elif line[i] == 'G':
                        profile['G'][0][i] += 1
                    else:
                        profile['T'][0][i] += 1

        for key in profile.keys():
            print key + ': ' + ''.join(str(list(profile[key][0][:])))

        consensus = []
        for i in range(dna_length):
            temp=[]
            for key in profile.keys():
                temp.append(profile[key][0][i])
            max_base = temp.index(max(temp))
            if max_base == 0:
                consensus.append('A')
            elif max_base == 1:
                consensus.append('C')
            elif max_base == 2:
                consensus.append('G')
            else:
                consensus.append('T')

        print ''.join(consensus)

        return None

    def dna_motif(self, file_name):
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

    def rna_to_protein(self, file_name):
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

    def permutations(self, i):
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

    def first_mendel(self, k, m, n):
        '''calculate probability that from 3 gene pairs DD Dd dd, there will be offspring
        with a dominant allele'''
        k, m, n = float(k), float(m), float(n)
        total = (k + m + n)*2  # total number of alleles
        num_dom = k*2 + m  # number of dominant
        num_rec = m + n*2  # number of recessive

        # probability of an offspring with >=1 dominant allele
        prob = (num_dom/total) * (num_dom-1)/(total-1) + ((num_dom/total) *
               (num_rec/(total-1))) + ((num_rec/total) * (num_dom/(total-1)))

        return prob

if __name__ == '__main__':
    ros = Rosalind()
    print ros.first_mendel(3,3,3)