from typing import List


class SolutionFour:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        amount = len(nums)
        if amount % 2 == 0:
            return (nums[amount // 2 - 1] + nums[amount // 2]) / 2
        else:
            return float(nums[amount // 2])
