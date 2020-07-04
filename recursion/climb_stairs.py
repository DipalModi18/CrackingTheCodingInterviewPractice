# Reference: https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1662/


class Solution(object):
    cache = {1: 1, 2: 2}
    # If person has to reach to the top at 1 step: total 1 possibility
    # If the person has to reach to the top at 2 step: total 2 possibility -- { 1+1, 2}
    # If the person has to reach to the top at 2 step: total 3 possibility -- { 1+1+1, 2+1, 1+2}
    #   i.e. adding +1 after every possibility of 2 and +2 after every possibility of 1
    #   so total possibilities for 3 are total possibilities of 1 and 2

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.cache:
            return self.cache[n]
        else:
            sol = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.cache[n] = sol
            return sol


if __name__ == "__main__":
    print(Solution().climbStairs())
