class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(current_list):
            if len(current_list) == k:
                result.append(current_list[:])
            else:
                for i in range(1, n+1):
                    if len(current_list) > 0:
                        if i > current_list[-1]:
                            current_list.append(i)
                            backtrack(current_list)
                            current_list.pop()
                        else:
                            continue
                    else:
                        current_list.append(i)
                        backtrack(current_list)
                        current_list.pop()
        temp_list = []
        backtrack(temp_list)
        return result