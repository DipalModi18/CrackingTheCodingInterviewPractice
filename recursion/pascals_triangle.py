# Problem statement: https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/3234/


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        prevSol = self.getRow(rowIndex - 1)
        sol = [None] * (rowIndex + 1)
        for i in range(0, rowIndex + 1):
            if i == 0 or i == rowIndex:
                sol[i] = 1
            else:
                sol[i] = prevSol[i - 1] + prevSol[i]

        return sol


if __name__ == "__main__":
    print(Solution().getRow(4))