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
    turn = 'Maria'

    if len(nums) == 0 or nums is None or x <= 0 or x != len(nums):
        return None

    for nbr_round in range(x):
        n = nums[nbr_round]
        collection = [nbr for nbr in range(1, n+1)]

        while len(collection) > 1:
            prime_found = False
            # Check each number in the collection to find a prime
            for idx in range(len(collection)):
                if is_prime(collection[idx]):
                    prime = collection[idx]
                    collection = [r for r in collection if r % prime != 0]
                    prime_found = True
                    turn = 'Ben' if turn == 'Maria' else 'Maria'
                    break
            if not prime_found:
                break

        if turn == 'Maria':
            # No moves left for Maria
            ben += 1
        else:
            # No moves left for Ben
            maria += 1

    winner = 'Ben' if ben > maria else 'Maria' if ben < maria else None

    return winner
