class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { ")" : "(", "}" : "{", "]" : "[" }
        stack = []
        for el in s:
            if el in mapping:
                if len(stack) == 0 or stack[-1] != mapping[el]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(el)
        if len(stack)>0:
            return False
        else:
            return True