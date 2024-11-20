class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_str, left, right):
            if len(current_str) == 2 * n:
                result.append(current_str)
            else:
                if left < n:
                    backtrack(current_str + "(", left + 1, right)
                if left > right:
                    backtrack(current_str + ")", left, right + 1)
        
        backtrack("", 0, 0)
        return result
