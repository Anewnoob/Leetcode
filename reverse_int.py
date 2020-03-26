class Solution:
    def reverse_force(self, x: int) -> int:
        if -10 < x < 10:
            return x
        #to string
        str_x = str(x)
        if x < 0 : reverse_str = - int(str_x[:0:-1])
        else: reverse_str = int(str_x[::-1])

        return reverse_str if -2147483648 < reverse_str < 2147483647 else 0

test = Solution()
result = test.reverse_force(123)
print(result)