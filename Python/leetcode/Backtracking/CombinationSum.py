from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(currIdx, potentialSol):
            if currIdx >= len(candidates) or sum(potentialSol) > target:
                return
            if sum(potentialSol) == target:
                ans.append(potentialSol.copy())
                return
            potentialSol.append(candidates[currIdx])
            dfs(currIdx, potentialSol)
            potentialSol.pop()
            dfs(currIdx+1, potentialSol)

        ans = []
        dfs(0, [])
        return ans