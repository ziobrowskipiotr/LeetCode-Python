class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current_list = []
        def backtrack(current_list):
            if len(current_list)>0 and sum(current_list) == target:
                if sorted(current_list) not in result:
                    result.append(sorted(current_list[:]))
            else:
                if sum(current_list) < target:
                    for number in candidates:
                        current_list.append(number)
                        backtrack(current_list)
                        current_list.pop()
        backtrack(current_list)
        return result
