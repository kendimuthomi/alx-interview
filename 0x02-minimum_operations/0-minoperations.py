#!/usr/bin/python3
"""Method that checks the fewest number of operations that results in n Hs"""
def minOperations(n):
    """minimum operations"""
    if (n == 1):
        return 0
    for i in range(2, int(n ** 0.5)+1):
        if (n % 1) == 0:
            return i + minOperations(n // i)
    return n