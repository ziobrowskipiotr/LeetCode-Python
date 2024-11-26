class Solution:
    def calculate(self, s: str) -> int:
        def calculating(s, stack):
            i = 0
            while i < len(s):
                match s[i]:
                    case " ":
                        i += 1
                    case "+":
                        if not stack or type(stack[-1]) is not int:
                            i += 1
                        else:
                            stack.append(s[i])
                            i += 1
                    case "-":
                        if not stack or type(stack[-1]) is not int:
                            i += 1
                            stack.append(-int(s[i]))
                        else:
                            stack.append(s[i])
                        i += 1
                    case "(":
                        temp_tuple = calculating(s[i+1:], [])
                        if stack and stack[-1] == "+":
                            stack.pop()
                            stack.append(stack.pop()+temp_tuple[0])
                        elif stack and stack[-1] == "-":
                            stack.pop()
                            stack.append(stack.pop()-temp_tuple[0])
                        else:
                            stack.append(temp_tuple[0])
                        i += temp_tuple[1]
                    case ")":
                        print(stack)
                        return (stack[0], i+2)
                    case _:
                        num = ""
                        while i < len(s) and s[i] not in ["+", "-", "(", ")"]:
                            num += s[i]
                            i += 1
                        num = int(num)
                        if stack and stack[-1] == "+":
                            stack.pop()
                            stack.append(stack.pop()+num)
                        elif stack and stack[-1] == "-":
                            stack.pop()
                            stack.append(stack.pop()-num)
                        else:
                            stack.append(num)
            print(stack)
            return (stack[0], i)
        return calculating(s, [])[0]