class CQueue:

    def __init__(self):
        self.stack = []

    def appendTail(self, value: int) -> None:
        self.stack.append(value)

    def deleteHead(self) -> int:
        if not self.stack: return -1
        return self.stack.pop(0)


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
