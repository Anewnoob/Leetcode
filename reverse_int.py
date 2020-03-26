class Solution:
    def reverse_force(self, x: int) -> int:
        if -10 < x < 10:
            return x
        #to string
        str_x = str(x)
        if x < 0 : reverse_str = - int(str_x[:0:-1])
        else: reverse_str = int(str_x[::-1])

        return reverse_str if -2147483648 < reverse_str < 2147483647 else 0

    def reverse_better(
            self,
            x: int) -> int:

        y, res = abs(x), 0
        #<< 2进制左移31位
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10  # %取余数
            if res > boundry:
                return 0
            y //= 10                # 向下取整 除
        return res if x > 0 else -res

test = Solution()
result = test.reverse_force(123)
print(result)