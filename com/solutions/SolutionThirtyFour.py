from typing import List


class SolutionThirtyFour:
    def searchLeft(self, nums: List[int], target: int, left: int, right: int):
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        else:
            return -1

    def searchRight(self, nums: List[int], target: int, left: int, right: int):
        while left < right:
            mid = (left + right) // 2 + (left + right) % 2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
        if nums[right] == target:
            return right
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        else:
            return [self.searchLeft(nums, target, 0, len(nums) - 1), self.searchRight(nums, target, 0, len(nums) - 1)]
