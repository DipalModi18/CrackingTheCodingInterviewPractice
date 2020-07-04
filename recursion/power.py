# Reference: https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        prevSolN = n-1 if n > 0 else n + 1
        prevSol = self.myPow(x, prevSolN)
        sol = prevSol * x if n > 0 else prevSol / x
        return sol

    def pow(self, x, n):
        return x ** n


if __name__ == "__main__":
    sol = Solution()
    print("2^3: {}".format(sol.myPow(2, 3)))
    print("2^-3: {}".format(sol.myPow(2, -3)))
    print("Python operator: {}".format(sol.pow(2, 3)))
    print("Python operator: {}".format(sol.pow(2, -3)))
