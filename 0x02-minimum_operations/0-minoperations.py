#!/usr/bin/python3
"""Method that checks the fewest number of operations that results in n Hs"""


def minOperations(n):
    """
    A function that calculates the fewest number of operations
    needed to obtain exactly n H characters in a file.
    Args:
        n (int): Number of characters to be displayed.
    Returns:
        int: Number of minimum operations.
    """
    current = 1
    previous = 0
    operations = 0
    
    while current < n:
        remainder = n - current
        
        if remainder % current == 0:
            # If remainder is divisible by current, increment operations by 2
            previous = current
            current += previous
            operations += 2
        else:
            # Otherwise, increment operations by 1
            current += previous
            operations += 1
    
    return operations

