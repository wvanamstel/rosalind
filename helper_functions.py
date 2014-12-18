# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 18:12:15 2014

@author: w
"""

def read_fasta(file_name):
    '''
    IN: txt file in fasta format
    OUT: dictionary with key=header and value = dna string
    '''
    with open(file_name) as fin:
        content = fin.read().splitlines()
    fin.close()
    
    # read file into fasta dictionary
    fasta_dict = {}
    for line in content:
        if line[0] == '>':
            header = line[1:]
            fasta_dict[header] = ''
        else:
            fasta_dict[header] += line
            
    return fasta_dict
    
def read_codon(table='dna'):
    '''
    IN: txt file name of rna or dna codon table
    OUT: dict with key=codon; value=amino acid
    '''
    if table.lower() == 'dna':
        file_name = 'dna_codon_table.txt'
    else:
        file_name = 'rna_codon_table.txt'
        
    with open(file_name) as fin:
        content = fin.read().split()
    fin.close()
    
    codon_table = {}
    i = 0
    while i < len(content):
        codon_table[content[i]] = content[i + 1]
        i += 2
    
    return codon_table