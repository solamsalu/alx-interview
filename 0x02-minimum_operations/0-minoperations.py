#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Calculates the fewest number of operations needed to 
    result in exactly n H characters in a file  """
    if n <= 0:
        return 0
    operations = 0
    current = 1
    copied = False
    while current < n:
        if n % current == 0:
            operations += 2
            current *= 2
            copied = True  
        elif copied:
            operations += 1  
            current += current // 2  
        else:
            return 0
    return operations
