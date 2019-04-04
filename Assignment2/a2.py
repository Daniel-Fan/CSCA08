"""CSCA08 Assignment 2, Fall 2017
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
 Date: 2017/11/28
"""


class Marker_Not_Set_Error(Exception):
    '''the error represents that we did not set a marker'''


class Chromosome():
    '''a class representing a chromosome'''
    def __init__(self, pair):
        '''(Chromosome, int) -> NoneType
        make an object by initializing the instance variables
        REQ: 0 <= pair <= 22
        '''
        # every chromosome should have a pair number
        self._pair = pair
        # set a new empty dict to store the specific position and nucleotide
        self._pos_nucl = {}
        # set a new empty dict to store the marker with psotion
        self._marker_pos = {}
        # set a new empty dict to store the lm or rm bool with position
        self._pos_maternal = {}

    def get_pos_nucl(self):
        '''(Chromosome) -> dict
        return the self._pos_nucl
        '''
        return self._pos_nucl

    def set_maternal(self, position, is_lm):
        '''(Chromosome, int, bool) -> NoneType
        set a dict whose key is the position and value is the nucleotide
        REQ: position > 0
        '''
        self._pos_maternal[position] = is_lm

    def get_maternal(self):
        '''(Chromosome) -> dict
        return the pos_maternal dict
        '''
        return self._pos_maternal

    def set_by_pos(self, position, nucleotide):
        '''(Chromosome, int, str) -> NoneType
        set a dict whose key is the position and value is the nucleotide
        REQ: position > 0
        REQ: nucleotide shoule be the combination of "ATCG"
        '''
        self._pos_nucl[position] = nucleotide

    def set_marker(self, marker, position):
        '''(Chromosome, str, int) -> NoneType
        set a dict whose key is marker and value is the position
        REQ: position > 0
        REQ: marker should be a string
        '''
        self._marker_pos[marker] = position

    def set_by_marker(self, marker, nucleotide):
        '''(Chromosome, str, str) -> NoneType
        replace the value of marker with new nucleotide
        REQ: marker should be a string
        REQ: nucleotide shoule be the combination of "ATCG"
        '''
        # get the psotion where the marker represents
        position = self._marker_pos[marker]
        # replace the nucleotide with a new string
        self._pos_nucl[position] = nucleotide

    def get_by_pos(self, position):
        '''(Chromosome, int) -> str
        get the nucleotide in that position
        REQ: position > 0
        '''
        result_nucl = self._pos_nucl.get(position, '')
        return result_nucl

    def get_by_marker(self, marker):
        '''(Chromosome, str) -> str
        get the nucleotide which the marker represents
        '''
        # get the psotion which the marker in
        position = self._marker_pos[marker]
        # use get_by_pos methods to get the nucleotide in that position
        result_nucl = self.get_by_pos(position)
        return result_nucl


class Person():
    '''a class representing a person'''
    def __init__(self):
        '''(Person) -> NoneType
        make an object by initializing the instance variables
        REQ: personal_id shoule be a string
        '''
        # set a empty dict for pair chromosome
        self._pair_chr = {}
        # set a empty dict for marker pair
        self._marker_pair = {}

    def get_pair_dict(self):
        '''(Person) -> dict
        return the dict whose key is index of chromosome, value is chromosome
        '''
        return self._pair_chr

    def set_by_pos(self, pair, position, nucleotide):
        '''(Person, int, int, str) -> NoneType
        set a dict whose key is the pair and specific chromosome is the value
        REQ: 0 <= pair <= 22
        REQ: nucleotide should be the combination of A, T, C, G.
        '''
        # we have set a pair as the key in dict before
        if(pair in self._pair_chr.keys()):
            # use chromosome's method to set the nucleotide in that position
            self._pair_chr[pair].set_by_pos(position, nucleotide)
        # we have not set a pair as the key in the dict
        else:
            # set a new value whose key is pair that is a chromosome
            self._pair_chr[pair] = Chromosome(pair)
            # use chromosome's method to set the nucleotide in that position
            self._pair_chr[pair].set_by_pos(position, nucleotide)

    def set_marker(self, marker, pair, position):
        '''(Person, str, int, int) -> NoneType
        set a dict whose key is the marker and specific chromosome is the value
        REQ: 0 <= pair <= 22
        '''
        # set a new value whose key is marker that is a pair
        self._marker_pair[marker] = pair
        # we have set a pair as the key in dict before
        if(pair not in self._pair_chr.keys()):
            # set a new value whose key is pair that is a chromosome
            self._pair_chr[pair] = Chromosome(pair)
        # use chromosome's method to set the position under that marker
        self._pair_chr[pair].set_marker(marker, position)

    def set_by_marker(self, marker, nucleotide):
        '''(Person, str, str) -> NoneType
        replace the nucleotide under that marker with a new nucleotide
        REQ: nucleotide should be the combination of A, T, C, G.
        '''
        # we can find a marker in marker_chr dict
        if(marker in self._marker_pair.keys()):
            # get the value whose key is marker
            pair = self._marker_pair.get(marker)
            # use chromosome's method to set the nucleotide under that marker
            self._pair_chr[pair].set_by_marker(marker, nucleotide)
        # we cannot find a marker in dict
        else:
            raise Marker_Not_Set_Error

    def get_by_pos(self, pair, position):
        '''(Person, int, int) -> str
        get the nucleotide in that pair and position
        REQ: 0 <= pair <= 22
        '''
        result_nucl = self._pair_chr[pair].get_by_pos(position)
        return result_nucl

    def get_by_marker(self, marker):
        '''(Person, str) -> str
        get the nucleotide that is represented by marker
        '''
        # we can find a marker as the key in the dict
        if(marker in self._marker_pair.keys()):
            # get the pair whose key is marker
            pair = self._marker_pair.get(marker)
            # get the nucleotide under that marker
            result_nucl = self._pair_chr[pair].get_by_marker(marker)
            return result_nucl
        # we can not find a marker as the key in the dict
        else:
            raise Marker_Not_Set_Error

    def get_chromosome(self, pair):
        '''(Person, int) -> Chromosome
        get the sepcific pair chromosome
        REQ: 0 <= pair <= 22
        '''
        # we have the pair as the key in the dict
        if(pair in self._pair_chr.keys()):
            result_chr = self._pair_chr[pair]
        # we cannot find pair as the key in the dict
        # we create a Chromosome that has no specific nucleotide
        else:
            result_chr = Chromosome(pair)
        return result_chr

    def set_chromosome(self, pair, chromosome):
        '''(Person, int, Chromosome) -> NoneType
        the person will have the chromosome in that pair
        REQ: 0 <= pair <= 22
        '''
        self._pair_chr[pair] = chromosome

    def test(self, query):
        '''(Person, Query) -> bool
        return True iff the nucleotide which is setted in query is the same as
        the nucleotide in person
        '''
        # set a empty dict to store memory nucleotide
        memory_nucl = {}
        # initialize a result to be True
        result = True
        # get the query's pair dict
        query_pair = query.get_pair_query()
        # loop every key in the pair_chr dict
        for key_pair in query_pair:
            # the person has this pair chromosome
            if(key_pair in self._pair_chr):
                # get the relationship between position and nucleotide
                # in pair chromosome in query
                pair_pos_chr_query = query_pair[key_pair].get_pos_nucl()
                # get the relationship between position and nucleotide
                # in pair chromosome in Person
                pair_pos_chr_person = self._pair_chr[key_pair].get_pos_nucl()
                # compare the nucleotide in the same position
                # between query and person
                for key_position in pair_pos_chr_query:
                    # the person has the same position in the chromosome
                    if(key_position in pair_pos_chr_person):
                        # get the nucleotide in query
                        nucl_query = pair_pos_chr_query[key_position]
                        # get the nucleotide in person
                        nucl_person = pair_pos_chr_person[key_position]
                        # compare the nucleotide between person and query
                        if(nucl_query != nucl_person):
                            # find the number in nucl_query
                            # loop every character in nucl_query
                            for index in range(0, len(nucl_query)):
                                # the element is number
                                if(nucl_query[index].isdigit() is True):
                                    # the element is in the memory_nucl
                                    if(nucl_query[index] in memory_nucl):
                                        # the index is 0
                                        if(index == 0):
                                            # get the new nucl_query
                                            nucl_query =\
                                                memory_nucl[nucl_query[index]]\
                                                + nucl_query[1]
                                        # the index is 1
                                        elif(index == 1):
                                            # get the new nucl_query
                                            nucl_query =\
                                                nucl_query[0] +\
                                                memory_nucl[nucl_query[index]]
                                    # the element is not in the memory_nucl
                                    else:
                                        # pair the memory nucl to normal nucl
                                        memory_nucl[nucl_query[index]]\
                                            = nucl_person[index]
                                        # if the index is 0
                                        if(index == 0):
                                            # get the new nucl_query
                                            nucl_query\
                                                = memory_nucl[nucl_query
                                                              [index]] +\
                                                nucl_query[1]
                                        # the index is 1
                                        elif(index == 1):
                                            # get the new nucl_query
                                            nucl_query = nucl_query[0]\
                                                + memory_nucl[nucl_query
                                                              [index]]
                            # check again that whether the nucleotides are same
                            if(nucl_query != nucl_person):
                                result = False
        return result


class Query():
    '''a class representing a query'''
    def __init__(self):
        '''(Query) -> NoneType
        make an object by initializing the instance variables
        '''
        self._person = Person()

    def set_by_pos(self, pair, position, nucleotide):
        '''(Query, int, int, str) -> NoneType
        use the method in person class to set_by_pos
        set a dict whose key is the pair and specific chromosome is the value
        REQ: 0 <= pair <= 22
        REQ: nucleotide should be the combination of A, T, C, G.
        '''
        self._person.set_by_pos(pair, position, nucleotide)

    def set_marker(self, marker, pair, position):
        '''(Query, str, int, int) -> NoneType
        use the method in person class to set_marker
        set a dict whose key is the marker and specific chromosome is the value
        REQ: 0 <= pair <= 22
        '''
        self._person.set_marker(marker, pair, position)

    def set_by_marker(self, marker, nucleotide):
        '''(Query, str, str) -> NoneType
        use the method in person class to set_by_marker
        replace the nucleotide under that marker with a new nucleotide
        REQ: nucleotide should be the combination of A, T, C, G.
        '''
        self._person.set_by_marker(marker, nucleotide)

    def get_pair_query(self):
        '''(Query) -> dict
        return a dict whose key is pair value is chromosome
        '''
        return self._person.get_pair_dict()


class Male(Person):
    '''this is a class that represents a men'''
    def __init__(self, personnal_id):
        '''(Men, str) -> NoneType
        make an object by initializing the instance variables
        REQ: personal_id shoule be a string
        '''
        super().__init__()
        self._id = personnal_id


class Female(Person):
    '''this is a class that represents a women'''
    def __init__(self, personnal_id):
        '''(Men, str) -> NoneType
        make an object by initializing the instance variables
        REQ: personal_id shoule be a string
        '''
        super().__init__()
        self._id = personnal_id

    def procreate(self, father, binder):
        '''(Female, Male, Binder) -> Male or Female
        return a child that will be male or female.
        and inherit some chromosome pair position from father and mother
        '''
        # if the child is Female
        if(binder.get_gender_Male() is False):
            child = Female('child')
        # if the child is Male
        elif(binder.get_gender_Male() is True):
            child = Male('child')
        # set a new dict that is the pair_maternal, get from binder method
        self._pair_maternal = binder.get_maternal()
        # get every key and value in dictionary by loop
        for key in self._pair_maternal:
            # get the index of pair chromosome for child
            child_pair = key
            # get the dictionary from the pair Chromosome representing
            child_pos_maternal = self._pair_maternal[child_pair].get_maternal()
            # get the position and maternal in chromosome by loop
            for key_position in child_pos_maternal:
                # the parents' nucleotide is empty, raise error
                if(self.get_by_pos(child_pair, key_position) == '' or
                   father.get_by_pos(child_pair, key_position) == ''):
                    raise Parent_Chromosome_is_empty
                else:
                    # if the maternal is LM
                    if(child_pos_maternal[key_position] is True):
                        # gets mothers left nucleotide and father's right
                        # get the left nucleotide from mother
                        left_nucleotide =\
                            self.get_by_pos(child_pair, key_position)[0]
                        # get the right nucleotide from father
                        right_nucleotide =\
                            father.get_by_pos(child_pair, key_position)[1]
                        # get the child's nucleotide in this position
                        child_nucleotide = left_nucleotide + right_nucleotide
                    # if the maternal is RM
                    elif(child_pos_maternal[key_position] is False):
                        # gets mothers right nucleotide and mother's right
                        # get the left nucleotide from mother
                        left_nucleotide =\
                            father.get_by_pos(child_pair, key_position)[0]
                        # get the right nucleotide from father
                        right_nucleotide = \
                            self.get_by_pos(child_pair, key_position)[1]
                        # get the child's nucleotide in this position
                        child_nucleotide = left_nucleotide + right_nucleotide
                    # set the child's chromosome by method set_by_pos
                    child.set_by_pos(child_pair,
                                     key_position, child_nucleotide)
        return child


class Binder():
    '''this is a class that representing a binder'''
    def __init__(self):
        '''(Binder) -> NoneType
        make an object by initializing the instance variables
        '''
        # set a empty dict for pair chromosome
        self._pair_chr = {}

    def set_sex(self, gender):
        '''(Binder, str) -> NoneType
        we can know from the method which the offspring is male or female
        '''
        self._gender = gender

    def get_gender_Male(self):
        '''(Binder) -> bool
        return True iff the sex is Male
        '''
        # gender is Female
        if(self._gender == 'F'):
            result_sex = False
        # gender is Male
        elif(self._gender == 'M'):
            result_sex = True
        return result_sex

    def set_by_pos(self, pair, position, maternal):
        '''(Binder, int, int, str) -> NoneType
        set the chromosome pair position to be left maternal or right maternal
        REQ: maternal need to be 'LM' or 'RM'
        REQ: 0 <= pair <= 22
        '''
        # child gets the mothers left nucleotide and the father's right
        if(maternal == 'LM'):
            self._leftmaternal = True
        # child gets the father's left nucleotide and the mother's right
        elif(maternal == 'RM'):
            self._leftmaternal = False
        # we have set a pair as the key in dict before
        if(pair in self._pair_chr.keys()):
            # use chromosome's method to set the maternal in that position
            self._pair_chr[pair].set_maternal(position, self._leftmaternal)
        # we have not set a pair as the key in the dict
        else:
            # set a new value whose key is pair that is a chromosome
            self._pair_chr[pair] = Chromosome(pair)
            # use chromosome's method to set the maternal in that position
            self._pair_chr[pair].set_maternal(position, self._leftmaternal)

    def get_maternal(self):
        '''(Binder) -> dict
        return the pair_chr dict
        '''
        return self._pair_chr
