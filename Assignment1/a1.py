"""CSCA08 Assignment 1, Fall 2017
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
 Date: 2017/11/11
"""


def pair_model(nucleotide1, nucleotide2):
    '''(str, str) -> True
    the function return true iff two nucleotides can be paired
    A can pair with T and C can pair with G.
    REQ: nucleotide is single character that should only be A, T, G or C.
    >>> pair_model('A', 'T')
    True
    >>> pair_model('A', 'G')
    False
    '''
    # assume the result is False firstly
    result = False
    # nucleotide1 is A
    if(nucleotide1 == 'A'):
        # nucleotide2 is T
        if(nucleotide2 == 'T'):
            # two nucleotides can pair, result is True
            result = True
    # nucleotide1 is T
    elif(nucleotide1 == 'T'):
        # nucleotide2 is A
        if(nucleotide2 == 'A'):
            # two nucleotides can pair, result is True
            result = True
    # nucleotide1 is C
    elif(nucleotide1 == 'C'):
        # nucleotide2 is G
        if(nucleotide2 == 'G'):
            # two nucleotides can pair, result is True
            result = True
    # nucleotide1 is G
    elif(nucleotide1 == 'G'):
        # nucleotide2 is C
        if(nucleotide2 == 'C'):
            # two nucleotides can pair, result is True
            result = True
    # get the result
    return result


def pair_genes(gene1, gene2):
    '''(str, str) -> bool
    nucleotides from gene1 to pair-bond with the nucleotides from gene2.
    guanine will pair with cytosine, and adenine will pair with thymine,
    but other combinations will not pair.
    the function will return True iff gene1 and gene2 can pair.
    REQ: gene1 and gene2 should only contain A, T, G, C in strings
    >>> pair_genes('ATGCGTAGC', 'TACGCATCG')
    True
    >>> pair_genes('GCTAGTAC', 'CGTGACG')
    False
    '''
    # assume the result is True, two genes pair
    result_pair = True
    # assume the index in strings begins from 0
    index = 0
    # if two genes do not in the same length, they do not pair, result is False
    if(len(gene1) != len(gene2)):
        result_pair = False
    # loop two strings when index is less than length of genes
    # or result is True
    while(index < len(gene1) and result_pair is True):
        # if the nucleotides pair, using the funtion pair_model
        if(pair_model(gene1[index], gene2[index])):
            # let index increase 1
            index += 1
        # if the nucleotides cannot pair
        else:
            result_pair = False
    # when the loop finish, return the result
    return result_pair


def zip_length(gene):
    '''(str) -> int
    a gene to partially pair with itself,called zipping.
    nucleotides at either end of a gene form a pair bond,
    which may in turn allow the next nucleotides in from those genes to bond.
    the process continues until a pair of nucleotides do not form a bondreturns
    and return the maximum number of nucleotide pairs that this gene can zip.
    REQ: gene should only contain A, T, G, C in strings
    >>> zip_length('AGTGCGCACACT')
    4
    >>> zip_length('CGACG')
    2
    >>> zip_length('TAGCTA')
    3
    >>> zip_length('GTCAGCTAGCT')
    0
    '''
    # assmue the gene can zip in current index
    result_zip = True
    # front index begins from 0 and rear index begins from -1
    front_index = 0
    rear_index = -1
    # loop the gene from either end of gene when front_index is less than
    # half of the length of gene minus 1 and result_zip is True
    while(front_index < (len(gene) - 1) / 2 and result_zip is True):
        # if the nucleotides in gene[front_index] can pair with
        # the nucleotide in gene[rear_index]
        if(pair_model(gene[front_index], gene[rear_index])):
            # the front_index increases 1 and rear_index decreases 1
            front_index += 1
            rear_index -= 1
        # if the nucleotides cannot pair
        else:
            # result_zip is False
            result_zip = False
    # the maximum number of nucleotide pairs is equal to the front_index
    # return the front_index
    return front_index


def find_anchor(gene, start_anchor, end_anchor):
    '''(list, str, str) -> list
    function will find the lowest index in gene where it is the postition for
    start_anchor from either end of gene and the index of end_anchor
    return a list, the first element in list is the index of start_anchor,
    the second element in list is the index of end_anchor,
    the third element whether the order is positive
    REQ: elements in gene should be A, T, G, C.
    REQ: start_anchor and end_anchor should only contain A,T,G,C in strings
    >>> gene = ['A', 'C', 'G', 'T', 'C', 'A', 'T', 'A', 'G']
    >>> start_anchor = 'CG'
    >>> end_anchor = 'CA'
    >>> find_anchor(gene, start_anchor, end_anchor)
    [1, 4, True]
    '''
    # convert the list to string
    gene = ''.join(gene)
    # get the reserve gene
    reserve_gene = gene[::-1]
    # get the lowest index for start-anchor in gene
    index_of_start_anchor_in_positive_order = gene.find(start_anchor)
    # get the lowest index for start-anchor in reserve gene
    index_of_start_anchor_in_reserve_order = reserve_gene.find(start_anchor)
    # start anchor cannot be found in the positive gene
    if(index_of_start_anchor_in_positive_order == -1):
        # result_positive will be empty
        result_positive = []
    # start anchor can be found in the positive gene
    elif(index_of_start_anchor_in_positive_order != -1):
        # find the index of end anchor in gene
        index_of_end_anchor_in_positive_order =\
            gene.find(end_anchor, index_of_start_anchor_in_positive_order)
        # end anchor can be found in the gene
        if(index_of_end_anchor_in_positive_order != -1):
            # get the result of index of start ancor and end anchor
            # and whether the order is positive
            result_positive = [index_of_start_anchor_in_positive_order,
                               index_of_end_anchor_in_positive_order, True]
        # end anchor cannot be found in the gene
        else:
            result_positive = []
    # start anchor cannot be found in reserve_gene
    if(index_of_start_anchor_in_reserve_order == -1):
        # result_reserve will be empty
        result_reserve = []
    # start anchor can be found in the reserve gene
    elif(index_of_start_anchor_in_reserve_order != -1):
        # find the index of end anchor in gene
        index_of_end_anchor_in_reserve_order =\
            gene.find(end_anchor, index_of_start_anchor_in_reserve_order)
        # the end anchor can be found in the gene
        if(index_of_end_anchor_in_reserve_order != -1):
            # get the result of index of start ancor and end anchor in the list
            # and whether the order is positive
            result_reserve = [index_of_start_anchor_in_positive_order,
                              index_of_end_anchor_in_reserve_order, False]
        # end anchor cannot be found in the gene
        else:
            result_reserve = []
    # the result of positive and reserve orders are both empty
    if(result_positive == [] and result_reserve == []):
        # the result is empty
        result = []
    # the result of reserve is empty and result will be positive order
    elif(result_reserve == []):
        result = result_positive
    # the result of positive is empty and result will be reserve order
    elif(result_positive == []):
        result = result_reserve
    # the result of positive and reserve are neither empty
    else:
        # the positive order index of start anchor is lower
        if(result_positive[0] < result_reserve[0]):
            result = result_positive
        # the reserve order index of start anchor is lower
        elif(result_positive[0] < result_reserve[0]):
            result = result_reserve
        # the index of start anchor is same
        elif(result_positive[0] == result_reserve[0]):
            # the difference of index of start and end anchor
            # in positive order is smaller than or the same as reserve order
            if((result_positive[1]-result_positive[0]) <=
               (result_reserve[1]-result_reserve[0])):
                result = result_positive
            # the difference of index of start and end anchor
            # in reserve order is smaller than or the same as positive order
            elif((result_positive[1]-result_positive[0]) >
                 (result_reserve[1]-result_reserve[0])):
                result = result_reserve
    # get the result
    return result


def splice_gene(source, des, start_anchor, end_anchor):
    '''(list, list, str, str) -> None
    the function splices the subsequence of source between the anchor strings
    into des between the anchor strings. In order to do this, we need
    to find anchor sequences that are the same in both genes, and
    swap everything in between these anchor sequences
    REQ: elements in souce and des should be A, T, G, C.
    REQ: start_anchor and end_anchor should only contain A,T,G,C in strings
    >>> source = ['A', 'C', 'G', 'T', 'C', 'A', 'T', 'A', 'G']
    >>> des = ['C', 'G', 'A', 'C', 'A']
    >>> start_anchor = 'CG'
    >>> end_anchor = 'CA'
    >>> splice_gene(source, des, start_anchor, end_anchor)
    >>> source == ['A', 'T', 'A', 'G']
    True
    >>> des == ['C', 'G', 'T', 'C', 'A']
    True
    >>> source = ['A', 'C', 'G', 'T', 'C', 'A', 'T', 'A', 'G']
    >>> des = ['C', 'G', 'A', 'C', 'A']
    >>> start_anchor = 'CG'
    >>> end_anchor = 'TA'
    >>> splice_gene(source, des, start_anchor, end_anchor)
    >>> source == ['A', 'C', 'G', 'T', 'C', 'A', 'T', 'A', 'G']
    True
    >>> des == ['C', 'G', 'A', 'C', 'A']
    True
    >>> source = ['A', 'C', 'G', 'T', 'C', 'A', 'T', 'A', 'G']
    >>> des = ['C', 'G', 'A', 'C', 'A']
    >>> start_anchor = 'TG'
    >>> end_anchor = 'CA'
    >>> splice_gene(source, des, start_anchor, end_anchor)
    >>> source == ['A', 'C', 'G', 'T', 'C', 'A', 'T', 'A', 'G']
    True
    >>> des == ['C', 'G', 'A', 'C', 'A']
    True
    '''
    # assume is_change is True
    is_change = True
    # use the funtion to get the anchor in source
    anchor_in_source = find_anchor(source, start_anchor, end_anchor)
    # use the function to get the anchor in des
    anchor_in_des = find_anchor(des, start_anchor, end_anchor)
    # the anchor_in_source or in des is empty
    if(anchor_in_des == [] or anchor_in_source == []):
        is_change = False
    if(is_change is True):
        # use the function find the index of start_anchor in source
        start_anchor_in_source = anchor_in_source[0]
        # use the function find the index of end_anchor in source
        end_anchor_in_source = anchor_in_source[1]
        # use the function find the index of start_anchor in des
        start_anchor_in_des = anchor_in_des[0]
        # use the function find the index of end_anchor in des
        end_anchor_in_des = anchor_in_des[1]
        # is positive order in source
        if(anchor_in_source[2] is True):
            # get the subsequence in source from start_anchor to end_anchor
            subsequence = source[start_anchor_in_source:
                                 end_anchor_in_source + len(end_anchor)]
            # copy the source to a temp_source
            temp_source = source[:]
            # clear the source
            source.clear()
            # add the elements in temp_source one by one before the anchor
            for index in range(0,
                               len(temp_source[:start_anchor_in_source])):
                source.append(temp_source[index])
            # add the elements in temp_source one by one after the anchor
            for index in range(end_anchor_in_source +
                               len(end_anchor), len(temp_source)):
                source.append(temp_source[index])
        # is reserve order in source
        elif(anchor_in_source[2] is False):
            # get the reserve source
            reserve_source = source[::-1]
            # get the subsequence in source from start_anchor to end_anchor
            subsequence =\
                reserve_source[start_anchor_in_source:end_anchor_in_source +
                               len(end_anchor)]
            # rewrite the reserve_source,
            # delete the subsequence between anchor in reserve_source
            reserve_source = reserve_source[:start_anchor_in_source]
            reserve_source += reserve_source[end_anchor_in_source +
                                             len(end_anchor):]
            # reserve the reserve_source to a new source
            double_reserve_source = reserve_source[::-1]
            # clear the source
            source.clear()
            for index in range(0, len(double_reserve_source)):
                source.append(double_reserve_source[index])
        # is positive order in des
        if(anchor_in_des[2] is True):
            # copy the des to a temp_des
            temp_des = des
            # clear the des
            des.clear()
            # add the elements in temp_des
            # one by one before the anchor
            for index in range(0, len(temp_des[:start_anchor_in_des])):
                des.append(temp_des[index])
            # add the subsequence between anchor to des
            for index in range(0, len(subsequence)):
                des.append(subsequence[index])
            # add the elements in temp_des
            # one by one after the anchor
            for index in range(end_anchor_in_des +
                               len(end_anchor), len(temp_des)):
                des.append(temp_des[index])
        # is reserve order in des
        elif(anchor_in_des[2] is False):
            # get the reserve_des
            reserve_des = des[:start_anchor_in_des]
            reserve_des += subsequence
            reserve_des += des[:end_anchor_in_des + len(end_anchor)]
            # reserve the reserve_des to a new des
            double_reserve_des = reserve_des[::-1]
            # clear the des
            des.clear()
            for index in range(0, len(double_reserve_des)):
                des.append(double_reserve_des[index])


def get_length_mask(mask):
    '''(string) -> int
    find the actual length of a mask
    REQ: characters in mask should be A, T, G, C, [], number and *
    '''
    # assume the length of mask is o
    length = 0
    index = 0
    # loop every character in mask
    while(index < len(mask)):
        # character is upper
        if(mask[index] == 'A' or mask[index] == 'T' or mask[index] == 'G' or
           mask[index] == 'C'):
            length += 1
        # is *
        elif(mask[index] == '*'):
            length += 1
        # between []
        elif(mask[index] == '['):
            length += 1
            index_of_right_bracket = mask.find(']', index)
            index = index_of_right_bracket
        # character is number
        elif(mask[index].isdigit() is True):
            length = length + int(mask[index]) - 1
        index += 1
    return length


def match_mask(gene, mask):
    '''(str, str) -> int
    Masks pair with parts of genes, the pairing works in the same manner
    as normal gene pairing.
    the function returns the index of the first nucleotide in the sequence
    that is matched by the mask, or -1 if the mask does not match anywhere
    in the gene.
    REQ: characters in gene should be A, T, G, C.
    REQ: characters in mask should be A, T, G, C, [], number and *
    >>> gene = 'ATGCGATCATCGAT'
    >>> mask = 'G[CG]T'
    >>> match_mask(gene, mask)
    3
    >>> gene = 'ATGATGATG'
    >>> mask = 'T*[CT]'
    >>> match_mask(gene, mask)
    0
    >>> gene = 'GCTGATC'
    >>> mask = 'C[AC]'
    >>> match_mask(gene, mask)
    -1
    >>> gene = 'GCTGACCCTC'
    >>> mask = 'C[TC]G3'
    >>> match_mask(gene, mask)
    3
    >>> gene = 'GCTGAGATC'
    >>> mask = 'C[TC]3'
    >>> match_mask(gene, mask)
    3
    '''
    # assume the index of gene is 0
    index_gene = 0
    # assume the index of mask is 0
    index_mask = 0
    # get the actual length of mask
    mask_length = get_length_mask(mask)
    # compare the mask and gene
    # when index is less than the length of gene and mask
    while(index_gene < len(gene) and index_mask < len(mask)):
        # the current character in mask is '*'
        if(mask[index_mask] == '*'):
            # we can find the next character in gene and mask
            index_gene += 1
            index_mask += 1
        # the current character in mask is '['
        elif(mask[index_mask] == '['):
            # find the next ']' character in mask
            index_of_right_bracket = mask.find(']', index_mask)
            # get all the character between []
            string_of_character = mask[index_mask + 1: index_of_right_bracket]
            # compare the character in gene with all characters between []
            # assume not find the pair character
            is_pair = False
            # loop every character in []
            for element in string_of_character:
                # find the pair character
                if(pair_model(gene[index_gene], element)):
                    is_pair = True
            # character in gene pairs with one of characters between []
            if(is_pair is True):
                # find the next character in gene and next character after ']'
                index_gene += 1
                index_mask = index_of_right_bracket + 1
            # character in gene does not pair with characters between []
            else:
                # character in gene returns to the character after inisital one
                index_gene = index_gene - index_mask + 2
                # the index of mask return to the first one
                index_mask = 0
        # the current character in mask is 'A, T, G, C'
        elif(mask[index_mask] == 'A' or mask[index_mask] == 'C' or
             mask[index_mask] == 'T' or mask[index_mask] == 'G'):
            # compare the character in gene and mask
            # assume not find the pair character
            is_pair = False
            # find the pair character
            if(pair_model(gene[index_gene], mask[index_mask]) is True):
                is_pair = True
            # character in gene pairs to character in mask
            if(is_pair is True):
                # find the next charracter in gene and mask
                index_gene += 1
                index_mask += 1
            # character in gene does not pair with character in mask
            else:
                # character in gene returns to the character after inisital one
                index_gene = index_gene - index_mask + 1
                # the index of mask return to the first one
                index_mask = 0
        # the current caracter in mask is number
        elif(mask[index_mask].isdigit() is True):
            # get the number
            number = mask[index_mask]
            # get the length of number
            length = 1
            # find the character before the number
            character_mask = mask[index_mask - 1]
            # if the charracter is ] or next character is number, increase 1
            if(character_mask == ']' or character_mask == '*' or
               mask[index_mask + 1].isdigit() is True):
                index_gene = len(gene) + 10
            else:
                # loop number times to compare the character in gene and mask
                # set the loop time, we have already compare the character
                # before number in the last time
                time = 1
                # assume is_pair is True at first
                is_pair = True
                # copy the index_gene to a internal_index_gene
                internal_index_gene = index_gene
                while(time < int(number) and is_pair is True):
                    # compare the character in gene and mask
                    # character does not pair with the character in mask
                    if(pair_model(gene[internal_index_gene], character_mask)
                       is False):
                        is_pair = False
                    # character in gene pairs to character in mask this time
                    if(pair_model(gene[internal_index_gene], character_mask)
                       is True):
                        internal_index_gene += 1
                    time += 1
                # character in gene pairs to character in mask this time
                if(is_pair is True):
                    # find the next charracter in gene and mask
                    index_gene = internal_index_gene
                    index_mask += length
                # character in gene does not pair with character in mask
                else:
                    # character in gene returns to the character after one
                    index_gene = index_gene - index_mask + 1
                    # the index of mask return to the first one
                    index_mask = 0
    # we have matched the mask to parts of gene
    if(index_mask >= len(mask)):
        # get the lowest_index
        lowest_index = index_gene - mask_length
    # if there is no matched index in the gene
    else:
        # return -1 for no lowest_index
        lowest_index = -1
    return lowest_index


def process_gene_file(input_file, gene, mask):
    '''(io.TextIOWrapper) -> tuple
    input_file containing one gene per line, a gene and a mask.
    Returns a tuple (p, m, z) where p = the first gene that can
    pair with the input gene string, m = the first gene that matches
    the mask, and z = the longest gene zip
    REQ: input_file containing one gene per line
    REQ: characters in gene should be A, T, G, C.
    REQ: characters in mask should be A, T, G, C, [], number and *
    '''
    # assume the pair is not found
    is_pair = False
    # assume the mask is not found
    find_first_mask = False
    # loop evey line in the input_file
    for next_line in input_file:
        # strip every line
        next_line = next_line.strip()
        # if we do not find the pair gene
        if(is_pair is False):
            # whether the line is pair with gene
            pair_result = pair_genes(next_line, gene)
            if(pair_result is True):
                # pair is found
                is_pair = True
                # get the pair gene
                pair_gene = next_line
        # find the length that the gene can be zip and
        # if it is bigger than previous value, repalce it
        if(zip_length(next_line) > length):
            length = zip_length(next_line)
        # find lowest_index in the gene for the mask in the line
        lowest_index = match_mask(gene, mask)
        # mask is match the gene and it is the first
        if(lowest_index != -1 and find_first_mask is False):
            # get the first gene and find value become true
            first_mask_gene = next_line
            find_first_mask = True
    # is_pair is False, no pair gene found, pair_gene return -1
    if(is_pair is False):
        pair_gene = -1
    # no mask gene found, first_mask_gene return -1
    if(first_mask_gene is False):
        find_first_gene = -1
    # return the tuple
    return (pair_gene, first_mask_gene, length)
