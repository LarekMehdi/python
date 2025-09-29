"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    result = list()
    result.append(number)
    result.append(number+1)
    result.append(number+2)
    return result


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    result = list()
    for item in rounds_1:
        result.append(item)
    for item in rounds_2:
        result.append(item)
    return result


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    total = sum(hand)
    avg = total / len(hand)
    return avg


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    avg = (hand[0] + hand[-1]) / 2
    idx = len(hand) // 2
    median = hand[idx]
    real_avg = sum(hand) / len(hand)

    return real_avg == avg or real_avg == median


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    odd = hand[::2]
    even = hand[1::2]

    odd_avg = sum(odd) / len(odd)
    even_avg = sum(even) / len(even)

    return odd_avg == even_avg


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    last_card = hand[-1]
    print(last_card)
    if last_card == 11:
        result = hand[:-1]
        result.append(last_card * 2)
        return result

    return hand
