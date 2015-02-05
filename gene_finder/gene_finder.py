# -*- coding: utf-8 -*-
"""
@author: CAZATRON

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq
tester = load_seq("./data/X73525.fa")

def shuffle_string(s):
    """Shuffles the characters in the input string"""
    return ''.join(random.sample(s,len(s)))

def collapse(L):
    """converts a list of strings to a string by concatenating elements of the list"""

    output = ""
    for s in L:
        output = output + s

    return output


def findLongest(temp):
    longest1 = temp[0]
    j = 1

    while j < len(temp):
        if len(temp[j]) > len(longest1):
            longest1 = temp[j]
        j += 1

    return longest1


### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
        this is fine because it's easy to test T and G as well
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """

    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
        sufficient because it's a simple operation
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """

    reverse = ''

    for letter in dna:
        reverse = get_complement(letter) + reverse
    
    return reverse


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns the sequence up to but not including the first in frame stop codon.  If there is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
        added an extra test to note that if string doesn't start with ATG it will still return normally, and if no stop codon appears it returns the whole string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("GCTATCGGT")
    'GCTATCGGT'
    """

    stopindex = -1

    for i in range(0,len(dna)-2,3):
        codon = dna[i] + dna[i+1] + dna[i+2]
        
        if codon in ['TAG', 'TAA', 'TGA']:
            stopindex = i 
            return dna[0:stopindex]

    return dna



def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested ORFs in the given DNA sequence and returns them as a list.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
        this is sufficient; it finds multiple ORFs in one string, including one that doesn't close in-frame
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """

    res = []
    i = 0

    while i < len(dna)-2:
        codon = dna[i] + dna[i+1] + dna[i+2]
        if codon == 'ATG':
            temp = rest_of_ORF(dna[i:])
            i = i + len(temp)
            res.append(temp)
        i = i + 3
    return res


def find_all_ORFs(dna):
    """ Finds all non-nested ORFs in the given DNA sequence in all 3 possible frames and returns them as a list.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
        sufficient because it can find one ORF in every reading frame
    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """

    res = []

    for i in range(0,3):
        temp = collapse(find_all_ORFs_oneframe(dna[i:]))
        if temp!= '':
            res.append(temp)

    return res

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested ORFs in the given DNA sequence on both strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
        sufficient because it doesn't need much testing--just gathering results from inner functions
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """

    res = []

    res.append(collapse(find_all_ORFs(dna)))
    res.append(collapse(find_all_ORFs(get_reverse_complement(dna))))

    return res



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it as a string
        sufficient because it proves that it correctly identifies reverse complement as longer than the given string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """

    temp = find_all_ORFs_both_strands(dna)
    
    return findLongest(temp)



def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF"""
    longer = []

    for i in range (1, num_trials):
        dnb = shuffle_string(dna)
        longer.append(longest_ORF(dnb))

    return findLongest(longer)

    pass

def coding_strand_to_AA(dna):
    """ Computes the protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the input DNA fragment
        sufficient because it proves the function will work whether or not there is a whole number of codons in the string
        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
        """

    res = ''

    for i in range(0,len(dna)-2,3):
        codon = dna[i] + dna[i+1] + dna[i+2]
        t = aa_table[codon]
        res += t

    return res

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum length specified."""

    prelim = find_all_ORFs_both_strands(dna)
    res = []

    for a in range(0,len(prelim)):
        if len(prelim[a]) > threshold:
            res.append(prelim[a])

    return res

#d = gene_finder(tester, 30)
#print d
#f = coding_strand_to_AA(d[1])
#print f

if __name__ == "__main__":
    import doctest
    doctest.testmod()