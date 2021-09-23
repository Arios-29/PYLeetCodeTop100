from typing import List


class SolutionFortySix:
    def dfs(self, nums: List[int], state: List[int], ans: List[List[int]]):
        if len(state) == len(nums):
            ans.append(state)
        else:
            num = nums[len(state)]
            for i in range(len(state) + 1):
                nextState = state.copy()
                nextState.insert(i, num)
                self.dfs(nums, nextState, ans)

    def permute(self, nums: List[int]) -> List[List[int]]:
        state = []
        ans = []
        self.dfs(nums, state, ans)
        return ans
