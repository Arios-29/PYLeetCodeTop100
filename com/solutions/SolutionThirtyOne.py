from typing import List


class SolutionThirtyOne:
    def nextPermutation(self, nums: List[int]) -> None:
        index = -1
        for i in range(len(nums) - 1)[::-1]:
            if nums[i] < nums[i + 1]:
                index = i
                break
        if index == -1:
            nums.reverse()
        else:
            for i in range(index + 1, len(nums))[::-1]:
                if nums[i] > nums[index]:
                    nums[index], nums[i] = nums[i], nums[index]
                    break
            left = index + 1
            right = len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
