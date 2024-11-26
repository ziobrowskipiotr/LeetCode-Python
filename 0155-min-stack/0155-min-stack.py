class MinStack:

    def __init__(self):
        self.stack = []
        self.min_map = collections.defaultdict(list)

    def push(self, val: int) -> None:
        if not self.stack or val < self.min_map[self.stack[-1]][-1]:
            self.min_map[val] += [val]
        else:
            self.min_map[val] += [self.min_map[self.stack[-1]][-1]]    
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.min_map[self.stack[-1]].pop()
            self.stack.pop()
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.min_map[self.stack[-1]][-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()