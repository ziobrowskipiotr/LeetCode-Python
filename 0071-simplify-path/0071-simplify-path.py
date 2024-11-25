class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split("/")
        stack = []
        for el in directories:
            match el:
                case "":
                    continue
                case ".":
                    continue
                case "..":
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        continue
                case _:
                    stack.append(el)
        return "/"+"/".join(stack)