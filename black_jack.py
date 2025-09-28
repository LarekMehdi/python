"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if (card == 'K' or card == 'Q' or card == 'J'):
        return 10
    elif card == 'A':
        return 1
    
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    value_1 = value_of_card(card_one)
    value_2 = value_of_card(card_two)

    if value_1 > value_2:
        return card_one
    elif value_1 < value_2:
        return card_two
        
    return card_one, card_two
    


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if (card_one == 'A' or card_two == 'A'):
        return 1

    total = value_of_card(card_one) +value_of_card(card_two)

    if total + 11 <= 21:
        return 11
    
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    
    has_ace = card_one == 'A' or card_two == 'A'
    head = has_head(card_one, card_two)
    ten = card_one == '10' or card_two == '10'

    if (head and has_ace) or (has_ace and ten):
        return True
        
    return False 

def has_head(card_one, card_two):
    heads = ['J', 'Q', 'K']
    return card_one in heads or card_two in heads

def is_head(card):
    heads = ['J', 'Q', 'K'] 
    return card in heads

def same_card_value(card_one, card_two):
    if (card_one == card_two) or (is_head(card_one) and is_head(card_two)):
        return True
    else: return False 

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return same_card_value(card_one, card_two)
    


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    ace_value = value_of_ace(card_one, card_two)
    first_value = value_of_card(card_one)
    second_value = value_of_card(card_two)
    
    if card_one == 'A':
        first_value = ace_value
    if card_two == 'A':
        second_value = ace_value

    total = first_value + second_value

    return 9 <= total <= 11
        
