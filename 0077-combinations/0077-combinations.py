class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(current_list, start):
            if len(current_list) == k:
                result.append(current_list[:])
            else:
                for i in range(start, n+1):
                        current_list.append(i)
                        backtrack(current_list, i+1)
                        current_list.pop()
        temp_list = []
        backtrack(temp_list, 1)
        return result