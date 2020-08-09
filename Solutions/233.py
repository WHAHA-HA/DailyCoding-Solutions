"""
Problem:

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
"""


def fib(n):
    curr, last = 1, 0
    for _ in range(n - 1):
        curr, last = last + curr, curr
    return curr


# DRIVER CODE
for i in range(1, 11):
    print(f"Fib {i}:\t{fib(i)}")
