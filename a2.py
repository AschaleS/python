def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    dna_length = len(dna)
    return dna_length

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    if dna1 > dna2:
        return True
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

            
    return dna.count(nucleotide) 

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False
def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if DNA sequence in dna is valid (that is, it contains
    no characters other than 'A', 'T', 'C' and 'G'). Do not treat lower cases and
    and characters other than 'A', 'T', 'C', and 'G'.
    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('atcg')
    False
    '''

    for char in dna:
        if char not in 'ATCG':

            return False
        
    return True
        
            
def insert_sequence(dna1, dna2, num):
    ''' (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into
    the first DNA sequence at the given index. Assume num < len(dna1).
    >>> insert_sequence('pinple', 'eap', 3)
    pineapple
    >>> insert_sequence('CCGT', 'GC', 3)
    CCGGCT
    '''
   
    new_dna =  dna1[:num] + dna2 + dna1[num:]
    return new_dna

def get_complement(s):
    ''' (str) -> str

    Return the complement of string 's'. Given that 's' is 'A', 'T', 'C' or 'G'

    >>> get_complement('A')
    T
    >>> get_complement ('G')
    C
    '''

    if s == 'A':
        return 'T'
    elif s == 'T':
        return 'A'
    elif s == 'C':
        return 'G'
    elif s == 'G':
        return 'C'

def get_complementary_sequence(s):
    '''(str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CGAT')
    'GCTA'
    '''
    dna_sequence = ''

    for char in s:
        dna_sequence += get_complement(char)
        
##        
##        if char  == 'A':
##            dna_sequence = dna_sequence + 'T'
##        if char  == 'T':
##            dna_sequence = dna_sequence + 'A'
##        if char  == 'C':
##            dna_sequence = dna_sequence + 'G'
##        if char  == 'G':
##            dna_sequence = dna_sequence + 'C'


    return dna_sequence



    
    
