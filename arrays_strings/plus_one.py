# Problem: https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        end = len(digits) - 1
        rem = 1
        while end >= 0:
            ne = digits[end] + rem
            digits[end], rem = (ne) % 10, 1 if ne % 10 == 0 else 0
            if rem == 0:
                break
            end = end - 1
        if rem != 0:
            digits.insert(0, rem)
        return digits


if __name__ == "__main__":
    print("Added 1 to [1, 2, 3]: {}".format(Solution().plusOne([1, 2, 3])))
    print("Added 1 to [9, 9, 9]: {}".format(Solution().plusOne([9, 9, 9])))
