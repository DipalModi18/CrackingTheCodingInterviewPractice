# Reference: https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
# TODO: Incomplete


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        right_sum = 0
        left_sum = 0
        total_sum = sum(nums)
        for i in range(0, len(nums)):
            left_sum = 0 if i == 0 else left_sum + nums[i - 1]
            right_sum = (total_sum - nums[i]) if i == 0 else (right_sum - nums[i])
            if left_sum == right_sum:
                return i
        return -1


if __name__ == "__main__":
    print("Pivot Index: {}".format(Solution().pivotIndex(nums=[1, 7, 3, 6, 5, 6])))
