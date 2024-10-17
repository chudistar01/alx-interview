#!/usr/bin/python3
""" prime game project
"""


def isWinner(x, nums):
    """x - rounds
    nums - number list
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben = 0
    maria = 0

    max_num = max(nums)

    primes = [True] * (max_num + 1)
    primes[0], primes[1] = False, False

    for start in range(2, int(max_num ** 0.5) + 1):
        if primes[start]:
            for multiple in range(start*start, max_num + 1, start):
                primes[multiple] = False

    for num in nums:
        prime_count = sum(primes[:num + 1])
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    else:
        return None


def rm_multiples(ls, x):
    """removes multiple
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
