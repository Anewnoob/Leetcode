假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：

第 i 位的数字能被 i 整除
i 能被第 i 位上的数字整除
现在给定一个整数 N，请问可以构造多少个优美的排列？

class Solution:
    def countArrangement(self, N: int) -> int: 
        l = [0 for _ in range(N + 1)]
        def f(num):
            if num > N:
                return 1
            ret = 0
            for i in range(1, len(l)):
                if l[i] == 0 and (num % i == 0 or i % num == 0):
                    l[i] = num
                    ret += f(num + 1)
                    l[i] = 0
            return ret
        return f(1)
