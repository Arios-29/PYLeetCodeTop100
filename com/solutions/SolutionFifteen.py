from typing import List


class SolutionFifteen:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 0:
            return ans
        nums.sort()
        for a in range(len(nums) - 2):
            if a != 0 and nums[a] == nums[a - 1]:
                continue
            b = a + 1
            c = len(nums) - 1
            while b < c:
                if b != a + 1 and nums[b] == nums[b - 1]:
                    b += 1
                    continue
                if c != len(nums) - 1 and nums[c] == nums[c + 1]:
                    c -= 1
                    continue
                tmp = nums[a] + nums[b] + nums[c]
                if tmp < 0:
                    b += 1
                elif tmp == 0:
                    ans.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                else:
                    c -= 1
        return ans
