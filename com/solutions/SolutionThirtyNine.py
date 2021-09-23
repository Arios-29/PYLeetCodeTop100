from typing import List


class SolutionThirtyNine:
    def dfs(self, candidates: List[int], target: int, ans: List[List[int]], index: int, state: List[int], sum: int):
        if sum == target:
            ans.append(state)
        elif sum > target:
            pass
        else:
            for i in range(index, len(candidates)):
                nextState = state.copy()
                nextState.append(candidates[i])
                self.dfs(candidates, target, ans, i, nextState, sum + candidates[i])

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        start = []
        self.dfs(candidates, target, ans, 0, start, 0)
        return ans
