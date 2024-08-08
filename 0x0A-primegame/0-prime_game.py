#!/usr/bin/python3
""" Prime Game Interview Question """


def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def find_multiples(prime, array):
    """ Finds all multiples of the given prime number from the array."""
    return [x for x in array if x % prime == 0]


def isWinner(x, nums):
    """
        players are: Maria & Ben
    :param x: (int) the number of rounds.
    :param nums: (list) of (int) An array of n
    :return: The Name of the player that won the most rounds,
        or None if the winner cannot be determined.
    """
    winner = None
    maria = 0
    ben = 0
    maria_turn = True
    ben_turn = False

    if len(nums) < 1:
        return winner

    if x > len(nums):
        x = len(nums)

    for nbr_round in range(x):
        n = nums[nbr_round]
        collection = [nbr for nbr in range(1, n+1)]
        idx = 1

        while len(collection) != 1:
            if idx >= len(collection):
                break

            if maria_turn:
                # Maria's turn
                if is_prime(collection[idx]):
                    num = collection[idx]
                    collection.remove(num)
                    for mult in find_multiples(num, collection):
                        collection.remove(mult)
                    maria_turn = False
                    ben_turn = True
                else:
                    idx += 1
            elif ben_turn:
                # Ben's Turn
                if is_prime(collection[idx]):
                    num = collection[idx]
                    collection.remove(num)
                    for mult in find_multiples(num, collection):
                        collection.remove(mult)
                    ben_turn = False
                    maria_turn = True
                else:
                    idx += 1

        if maria_turn:
            # No moves left for Maria
            ben += 1
        else:
            # No moves left for Ben
            maria += 1

    if ben > maria:
        winner = 'Ben'
    elif ben < maria:
        winner = 'Maria'

    return winner
