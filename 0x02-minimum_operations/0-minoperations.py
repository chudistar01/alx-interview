#!/usr/bin/python3
"""python module"""


def minOperations(n):
    """
    GETS MINIMIUM
    """
    if n < 2:
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n //= root
            root -= 1
        root += 1
    return ops
