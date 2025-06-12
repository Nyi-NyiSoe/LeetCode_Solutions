"""
You are given positive integers n and m.

Define two integers as follows:

    num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
    num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.

Return the integer num1 - num2.
"""


class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = sum(x for x in range(1,n+1)if x % m !=0)
        num2 = sum(y for y in range(1,n+1)if y % m ==0)

        return num1 - num2 

        




