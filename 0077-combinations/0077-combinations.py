class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(current_list):
            if len(current_list) == k:
                result.append(current_list)
            else:
                for i in range(1, n+1):
                    if len(current_list) > 0:
                        if i > current_list[-1]:
                            temp = current_list[:]
                            temp.append(i)
                            backtrack(temp)
                        else:
                            continue
                    else:
                        temp = current_list[:]
                        temp.append(i)
                        backtrack(temp)
        temp_list = []
        backtrack(temp_list)
        return result