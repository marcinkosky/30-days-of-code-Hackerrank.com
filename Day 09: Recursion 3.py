#!/bin/python3

"""
Task
Write a factorial function that takes a positive integer, N as a parameter and /
prints the result of N! (N factorial).

Note:
If you fail to use recursion or fail to name your recursive function factorial /
or Factorial, you will get a score of 0.
"""

n = int(input())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

calculus = factorial(n)
print(calculus)
