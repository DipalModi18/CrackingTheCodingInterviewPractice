def reverse(s):
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if len(s) == 2:
            return [s[1], s[0]]
        solutionToSubproblem = self.reverseString(s[1:])
        solutionToSubproblem.append(s[0])
        return solutionToSubproblem

    def helper(self, s):
        self.reverseStringInPlace(s, 0, len(s)-1)

    def reverseStringInPlace(self, s, left, right):
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        left = left + 1
        right = right - 1
        self.reverseStringInPlace(s, left, right)


if __name__ == "__main__":
    s = "abcde"
    print("Reversed string of {} is {}".format(s, reverse("abcde")))
    print("Reverse string of list: {}".format(Solution().reverseString(["a", "b", "c", "d", "e"])))

    # Reference: https://leetcode.com/articles/reverse-string/
    ss = ["a", "b", "c", "d", "e"]
    Solution().helper(ss)
    print("Reverse string which does not take extra memory: {}".format(ss))
