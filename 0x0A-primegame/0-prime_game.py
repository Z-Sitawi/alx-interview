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


def remove_multiples(arr, prime):
    """Mark multiples of the given prime as non-prime in the array."""
    for i in range(prime * 2, len(arr), prime):
        arr[i] = 0


def isWinner(x, nums):
    """
    Determine which player won the most rounds.
    :param x: (int) the number of rounds.
    :param nums: (list) of (int) An array of n
    :return: The name of the player that won the most rounds,
             or None if the winner cannot be determined.
    """
    maria_wins = 0
    ben_wins = 0

    if x <= 0 or not nums:
        return None

    # Limit the number of rounds to the number of available games
    x = min(x, len(nums))

    # Create a boolean list to mark primes
    max_n = max(nums)
    is_prime_list = [1] * (max_n + 1)  # 1 means active
    is_prime_list[0], is_prime_list[1] = 0, 0  # 0 and 1 are not primes

    # Mark non-prime numbers using the sieve method
    for i in range(2, len(is_prime_list)):
        if is_prime_list[i] == 1:  # i is a prime number
            remove_multiples(is_prime_list, i)

    for n in nums:
        # Determine if the count of active numbers up to n is even or odd
        if sum(is_prime_list[:n + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
