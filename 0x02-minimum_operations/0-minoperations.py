#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    # If n is less than or equal to 0, return 0
    if n <= 0:
        return 0
    # Initialize the number of operations to 0
    operations = 0
    # Initialize the current number of H characters to 1
    current = 1
    # Initialize a flag to indicate whether we have copied or not
    copied = False
    # Loop until we reach n
    while current < n:
        # If n is divisible by the current number, copy all and paste
        if n % current == 0:
            operations += 2  # Copy all and paste are two operations
            current *= 2  # Double the current number of H characters
            copied = True  # Set the flag to true
        # Otherwise, paste the copied number if we have copied before
        elif copied:
            operations += 1  # Paste is one operation
            current += current // 2  # Add half of the current number of H characters
        # Otherwise, we cannot achieve n with the given operations, return 0
        else:
            return 0
    # Return the number of operations
    return operations
