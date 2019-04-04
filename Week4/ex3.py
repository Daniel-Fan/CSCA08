def percent_to_gpv(percentage_mark):
    ''' (int) -> float
    The function takes a mark and return GPV
    REQ: 0 <= percentage_mark <= 100
    REQ: 0.0 <= GPV <= 4.0
    >>> percent_to_gpv(87)
    4.0
    >>> percent_to_gpv(60)
    1.7
    '''
    # the mark which is higher than or equal to 85
    if(percentage_mark >= 85):
        GPV = 4.0
    # the mark which is higher than or equal to 80 but less than 85
    elif(percentage_mark >= 80):
        GPV = 3.7
    # the mark which is higher than or equal to 77 but less than 80
    elif(percentage_mark >= 77):
        GPV = 3.3
    # the mark which is higher than or equal to 73 but less than 77
    elif(percentage_mark >= 73):
        GPV = 3.0
    # the mark which is higher than or equal to 70 but less than 73
    elif(percentage_mark >= 70):
        GPV = 2.7
    # the mark which is higher than or equal to 67 but less than 70
    elif(percentage_mark >= 67):
        GPV = 2.3
    # the mark which is higher than or equal to 63 but less than 67
    elif(percentage_mark >= 63):
        GPV = 2.0
    # the mark which is higher than or equal to 60 but less than 63
    elif(percentage_mark >= 60):
        GPV = 1.7
    # the mark which is higher than or equal to 57 but less than 60
    elif(percentage_mark >= 57):
        GPV = 1.3
    # the mark which is higher than or equal to 53 but less than 57
    elif(percentage_mark >= 53):
        GPV = 1.0
    # the mark which is higher than or equal to 50 but less than 53
    elif(percentage_mark >= 50):
        GPV = 0.7
    # the mark which is higher than or equal to 0 but less than 50
    elif(percentage_mark >= 0):
        GPV = 0.0
    return GPV


def card_namer(card_value, card_suit):
    ''' (str, str) -> str
    The function input the value and suit of card and return full name of card
    REQ: card_value = "A", "2...9", "T", "J", "Q", "K"
    REQ: card_suit can be any string
    >>> card_namer('Q', 'D')
    'Queen of Diamonds'
    >>> card_namer('9', 'S')
    '9 of Spades'
    >>> card_namer('8', 'T')
    'CHEATER!'
    '''
    # choose the value A
    if(card_value == 'A'):
        # value A to Ace
        card_value = 'Ace'
    # choose the value T
    elif(card_value == 'T'):
        # value T to 10
        card_value = '10'
    # choose the value J
    elif(card_value == 'J'):
        # value J to Jack
        card_value = 'Jack'
    # choose the value Q
    elif(card_value == 'Q'):
        # value Q to Queen
        card_value = 'Queen'
    # choose the value K
    elif(card_value == 'K'):
        # value K to King
        card_value = 'King'
    # choose suit D
    if(card_suit == 'D'):
        # suit D to Diamonds
        card_suit = 'Diamonds'
        # get the full name
        full_name = card_value + ' ' + 'of' + ' ' + card_suit
    # choose suit C
    elif(card_suit == 'C'):
        # suit C to Clubs
        card_suit = 'Clubs'
        # get the full name
        full_name = card_value + ' ' + 'of' + ' ' + card_suit
    # choose suit H
    elif(card_suit == 'H'):
        # suit H to Hearts
        card_suit = 'Hearts'
        # get the full name
        full_name = card_value + ' ' + 'of' + ' ' + card_suit
    # choose suit S
    elif(card_suit == 'S'):
        # suit S to Spades
        card_suit = 'Spades'
        # get the full name
        full_name = card_value + ' ' + 'of' + ' ' + card_suit
    # suit is not one of recognized inputs
    else:
        # it is a cheater
        full_name = 'CHEATER!'
    # return the full_name
    return full_name
