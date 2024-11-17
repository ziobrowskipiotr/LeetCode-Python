class Solution:
    def __init__(self):
        self.result = []
        self.keyboard_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:

        def backtrack(i, current_string):
            if len(current_string) == len(digits):
                self.result.append(current_string)
            else:
                for alpha in self.keyboard_map[digits[i]]:
                    backtrack(i+1, current_string + alpha)

        if digits:
            backtrack(0, "")
        return self.result