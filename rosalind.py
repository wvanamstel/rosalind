'''
Created on Jun 24, 2014

@author: w
'''
import itertools
import math
import numpy as np
import re
import helper_functions as hf


class Rosalind(object):
    def __init__(self):
        pass

    def consensus_and_profile(self, file_name):
        '''construct consensus list and profile matrix from a number
        of dna strings, input is FASTA style'''

        with open(file_name) as fin:
            content = fin.read().splitlines()
        fin.close()

        profile = {'A': np.zeros((1, 1000)),
                   'C': np.zeros((1, 1000)),
                   'G': np.zeros((1, 1000)),
                   'T': np.zeros((1, 1000))}

        dna_string = ''

        for line in content:
            if line[0] == '>' and dna_string != '':
                dna_length = len(dna_string)
                for i in range(dna_length):
                    if dna_string[i] == 'A':
                        profile['A'][0][i] += 1
                    elif dna_string[i] == 'C':
                        profile['C'][0][i] += 1
                    elif dna_string[i] == 'G':
                        profile['G'][0][i] += 1
                    else:
                        profile['T'][0][i] += 1
                dna_string = ''
            elif line[0] != '>':
                dna_string += line

        # include the last line in the file as well
        for i in range(dna_length):
                    if dna_string[i] == 'A':
                        profile['A'][0][i] += 1
                    elif dna_string[i] == 'C':
                        profile['C'][0][i] += 1
                    elif dna_string[i] == 'G':
                        profile['G'][0][i] += 1
                    else:
                        profile['T'][0][i] += 1

        # make consensus dna string
        consensus = []
        for i in range(dna_length):
            consensus.append(max(profile.iterkeys(),
                                 key=(lambda key: profile[key][0][i])))

        # print output in acceptable format
        print ''.join(consensus)

        A_temp = 'A: '
        C_temp = 'C: '
        G_temp = 'G: '
        T_temp = 'T: '
        for i in range(dna_length):
            A_temp += str(int(profile['A'][0][i])) + ' '
            C_temp += str(int(profile['C'][0][i])) + ' '
            G_temp += str(int(profile['G'][0][i])) + ' '
            T_temp += str(int(profile['T'][0][i])) + ' '

        print A_temp
        print C_temp
        print G_temp
        print T_temp

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
                sub_string_pos = dna_string.find(sub_string, i) + 1
                i = sub_string_pos
                positions += str(sub_string_pos) + ' '
            i += 1

        return positions

    def rna_to_protein(self, file_name):
        fin = open(file_name, 'r')
        content = fin.read()
        fin.close()
        codons = re.findall(r'.{1,3}', content, re.DOTALL)
        # split 3 letter codons from string

        fin = open('codon_table.txt', 'r')  # load codon table and put in dict
        codon_list = fin.read().split()
        fin.close()
        codon_table = {}
        i = 0
        while i < len(codon_list):
            codon_table[codon_list[i]] = codon_list[i + 1]
            i += 2

        protein_string = '' # construct protein string using codons and codon table
        for codon in codons:
            if(codon_table[codon] == 'Stop'):
                break
            protein_string += codon_table[codon]

        return protein_string

    def permutations(self, i):
        j = range(1, i + 1)

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
        num_rec = m + n*2  # number of recessive com

        # probability of an offspring with >=1 dominant allele
        prob = (num_dom/total) * (num_dom-1)/(total-1) + ((num_dom/total) *
               (num_rec/(total-1))) + ((num_rec/total) * (num_dom/(total-1)))

        return prob

    def overlap(self, file_name):
        # read fasta
        fasta_dict = hf.read_fasta(file_name)

        # determine all permutations of strings and determine overlap
        for pair in itertools.permutations(fasta_dict.keys(), 2):
            if fasta_dict[pair[0]][-3:] == fasta_dict[pair[1]][:3]:
                print pair[0], pair[1]

    def expected_offspring(self, file_name):
        with open(file_name) as fin:
            offspring = fin.read().split(' ')
        fin.close()

        offspring = [int(i) for i in offspring]
        expected_offspring = [2., 2., 2., 1.5, 1, 0]
        print sum([x * y for x, y in zip(offspring, expected_offspring)])

    def shared_motif(self, file_name):
        # find largest shared motif in dna strings
        dna_dict = hf.read_fasta(file_name)
        dna_list = dna_dict.values()
        shortest_dna = min(dna_list, key=len)

        # start at largest substring and work down to find matches
        found = False
        for i in range(len(shortest_dna), 1, -1):
            for j in range(len(shortest_dna) - i, -1, -1):
                if found:
                    break
                sub = shortest_dna[j:j+i]
                if all(sub in dna for dna in dna_list):
                    found = True
                    print sub

    def indep_alleles(self, k, N):
        

if __name__ == '__main__':
    ros = Rosalind()
    ros.shared_motif('rosalind_lcsm.txt')