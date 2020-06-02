求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

class Solution:
    def __init__(self):
        self.sum_all = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.sum_all += n
        return self.sum_all
