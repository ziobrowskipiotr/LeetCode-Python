class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        result = 0
        sign = 1
        operand = 0

        for ch in s:

            if ch.isdigit():
                operand = (operand * 10) + int(ch)

            elif ch == "+":
                result += sign*operand
                sign = 1
                operand = 0

            elif ch == "-":
                result += sign*operand
                sign = -1
                operand = 0

            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif ch == ")":
                result += sign*operand
                sign = stack.pop()
                result = sign*result
                result += stack.pop()
                operand = 0
                sign = 1
            
            else:
                continue

        return result + sign*operand