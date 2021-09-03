from typing import List


class SolutionOne:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aMap = {}
        size = len(nums)
        for i in range(size):
            left = target - nums[i]
            if left in aMap:
                answer = [aMap.get(left), i]
                break
            else:
                aMap[nums[i]] = i
        return answer
