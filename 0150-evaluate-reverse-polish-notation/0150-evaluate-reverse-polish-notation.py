class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            match element:
                case "+":
                    new_element = stack[-1]
                    stack.pop()
                    new_element += stack[-1]
                    stack.pop()
                    stack.append(new_element)
                    print(new_element)
                case "-":
                    new_element = stack[-1]
                    stack.pop()
                    new_element = stack[-1] - new_element
                    stack.pop()
                    stack.append(new_element)
                    print(new_element)
                case "*":
                    new_element = stack[-1]
                    stack.pop()
                    new_element *= stack[-1]
                    stack.pop()
                    stack.append(new_element)   
                    print(new_element)
                case "/":
                    new_element = stack[-1]
                    stack.pop()
                    new_element = trunc(stack[-1]/new_element)
                    stack.pop()
                    stack.append(new_element)
                    print(new_element)
                case _:
                    stack.append(int(element))
        return stack[0]                           