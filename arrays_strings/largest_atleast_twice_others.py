# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = nums[0]
        second_largest = 0
        index = 0
        for i in range(0, len(nums)):
            if largest < nums[i]:
                second_largest = largest
                largest = nums[i]
                index = i
            elif second_largest < nums[i] != largest:
                second_largest = nums[i]
            elif second_largest == largest:
                # [6, 6, 6, 5] => Here for when num = 5 at that time largest and second largest would be 6
                second_largest = nums[i]
        print(largest, second_largest)
        if largest >= second_largest * 2:
            return index
        else:
            return -1


if __name__ == "__main__":
    print("Index: {}".format(Solution().dominantIndex([0,0,2,3])))
