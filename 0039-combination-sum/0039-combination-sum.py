class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current_list = []
        len_cand = len(candidates)
        def backtrack(current_list, i, suma):
            if i >= len_cand:
                return
            elif len(current_list)>0 and suma == target:
                print(current_list)
                result.append(current_list[:])
                return
            else:
                if suma < target:
                    current_list.append(candidates[i])
                    backtrack(current_list, i, suma+candidates[i])
                    current_list.pop()
                    backtrack(current_list, i+1, suma)
        backtrack(current_list, 0, 0)
        return result
