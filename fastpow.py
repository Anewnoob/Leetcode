实现 pow(x, n) ，即计算 x 的 n 次幂函数。

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0 :
            x,n = 1/x, -n
        while n > 0:
            if n % 2 == 1:
               res = res * x
            x *= x
            n = n // 2 
        return res 
