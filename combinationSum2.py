class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        results = []

        def backtrack(start, path, target):
            if target == 0:
                results.append(path)
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > target:
                    break
                
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])

        backtrack(0, [], target)
        return results
    
    
    
# Advanced 
# class Solution:
#     def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
#         candidates.sort()
#         dp = [set() for _ in range(target + 1)]
#         dp[0].add(())

#         for num in candidates:
#             for t in range(target, num - 1, -1):
#                 for comb in dp[t - num]:
#                     dp[t].add(comb + (num,))
        
#         return [list(comb) for comb in dp[target]]