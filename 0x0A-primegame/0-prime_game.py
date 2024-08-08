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
    maria = 0
    ben = 0
    turn = 'M'
    x = min(x, len(nums))

    if len(nums) < 1 or not nums:
        return None

    for nbr_round in range(x):
        n = nums[nbr_round]
        collection = [nbr for nbr in range(1, n+1)]
        idx = 1

        while len(collection) > 1:
            if idx >= len(collection):
                break

            if is_prime(collection[idx]):
                num = collection[idx]
                collection.remove(num)
                for mult in find_multiples(num, collection):
                    collection.remove(mult)
                turn = 'B' if turn == 'M' else 'B'
            else:
                idx += 1

        if turn == 'M':
            # No moves left for Maria
            ben += 1
        else:
            # No moves left for Ben
            maria += 1

    winner = 'Ben' if ben > maria else 'Maria' if ben < maria else None

    return winner
