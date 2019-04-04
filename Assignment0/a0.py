"""CSCA08 Assignment 0, Fall 2017

 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name: Yuchen Fan
 UtorID: fanyuch1
 Student Number: 1003800265
 Date: 10/10/2017
"""


def split_input(DNA_sequence):
    """(str) -> list
    The function takes in a sequence and return three elements
    REQ: the element in the DNA_sequence should be 'A' or 'G' or 'T' or 'C'
    >>> split_input('TCGACCATGGCTAATGCGA')
    ['TCGACC', 'ATGGCTA', 'ATGCGA']
    >>> split_input('TCGACCATGGCT')
    ['TCGACC', '', 'ATGGCT']
    """
    # find the lowest index of 'ATG' in the sequence
    lowest_index = DNA_sequence.index('ATG')
    # find the next index of 'ATG' in the sequence
    next_index = DNA_sequence.find('ATG', lowest_index + 3)
    # upstream_data is from the beginning to lowest_index
    upstream_data = DNA_sequence[:lowest_index]
    # if the next_index is not found
    if(next_index == -1):
        # the_gene is an empty string
        the_gene = ''
        # downstream_data is from lowest_index to the end
        downstream_data = DNA_sequence[lowest_index:]
    else:
        # the_gene is from lowest_index to next_index
        the_gene = DNA_sequence[lowest_index:next_index]
        # downstream_data is from next_index to the end
        downstream_data = DNA_sequence[next_index:]
    # the three strings are three elements in the list
    split_sequence = [upstream_data, the_gene, downstream_data]
    return split_sequence


def get_gene(DNA_sequence):
    '''(str) -> str
    take a sequence and get the gene if it is present or return error
    REQ: the element in the DNA_sequence should be 'A' or 'G' or 'T' or 'C'
    >>> get_gene('GATCATGCCTGAAGATGGCCTA')
    'ATGCCTGAAG'
    >>> get_gene('ATTGGCGATCATGAA')
    'ERROR'
    '''
    # find the lowest index of 'ATG' in the sequence
    lowest_index = DNA_sequence.index('ATG')
    # find the next index of 'ATG' in the sequence
    next_index = DNA_sequence.find('ATG', lowest_index + 3)
    # if the next_index is not found
    if(next_index == -1):
        # the gene is not present
        the_gene = 'ERROR'
    else:
        # the gene is from lowest_index to next_index
        the_gene = DNA_sequence[lowest_index:next_index]
    return the_gene


def validate_gene(the_gene):
    '''(str) -> bool
    the function return True iff the gene is valid
    REQ: the element in gene is 'A' or 'G' or 'T' or 'C'
    >>> validate_gene('ATGGCTAAT')
    True
    >>> validate_gene('ATTGGTGTGC')
    False
    '''
    # the start with the start codon and there is no ATG at the middle of gene
    if(the_gene.find('ATG') != 0 or the_gene.rfind('ATG') != 0):
        result = False
    # contain at least one codon after the start codon
    elif(len(the_gene) < 6):
        result = False
    # contain only full codons
    elif(len(the_gene) % 3 != 0):
        result = False
    # never contain four consecutive identical nucleotides
    elif(the_gene.rfind('AAAA') != -1 or the_gene.rfind('GGGG') != -1 or
         the_gene.rfind('CCCC') != -1 or the_gene.rfind('TTTT') != -1):
        result = False
    # the gene is valid
    else:
        result = True
    return result


def is_palindromic(the_gene):
    '''(str) -> bool
    if the gene is palindromic, return true
    REQ: the element in gene is 'A' or 'G' or 'T' or 'C'
    >>> is_palindromic('ATGGCGGTA')
    True
    >>> is_palindromic('ATGGGCACG')
    False
    '''
    # reverse the gene
    reversed_gene = the_gene[::-1]
    # if the gene is palindromic
    if(reversed_gene == the_gene):
        if_palidromic = True
    else:
        if_palidromic = False
    # return the value
    return if_palidromic


def evaluate_sequence(DNA_sequence):
    '''(str) -> str
    Takes in a DNA sequence and returns the appropriate strings
    >>> evaluate_sequence('ACGTATGCGCGTAATGTC')
    'Valid Palindromic Gene Found'
    >>> evaluate_sequence('AATGTGA')
    'No Gene Found'
    >>> evaluate_sequence('ATGGGGCATGTTGCG')
    'Invalid Gene'
    '''
    # get the gene from the DNA_sequence
    the_gene = get_gene(DNA_sequence)
    # the gene is not present
    if(the_gene == 'ERROR'):
        evaluate = "No Gene Found"
    # the gene is valid and palindromic
    elif(is_palindromic(the_gene) and validate_gene(the_gene)):
        evaluate = "Valid Palindromic Gene Found"
    # the gene is valid
    elif(validate_gene(the_gene)):
        evaluate = "Valid Gene Found"
    # the gene is not valid
    else:
        evaluate = "Invalid Gene"
    # return the evaluation
    return evaluate
