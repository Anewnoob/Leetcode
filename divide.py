#给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

#返回被除数 dividend 除以除数 divisor 得到的商。

#整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return None
        flag = 0
        count = 0
        b = 1
        if dividend*divisor < 0:
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0
        while dividend >= divisor:
            dividend -= divisor
            count += 1
        if flag == 1:
            return -count
        return count
        
