# Fibonacci series using memoization
# Reference: https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/


class Solution(object):
    cache = {}

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0 or N == 1:
            return N
        elif N in self.cache:
            return self.cache[N]
        else:
            return self.fib(N - 1) + self.fib(N - 2)
