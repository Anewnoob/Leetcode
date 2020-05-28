#给定一个经过编码的字符串，返回它解码后的字符串。
#s = "3[a]2[bc]", 返回 "aaabcbc".
#s = "3[a2[c]]", 返回 "accaccacc".
#s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".


class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        n = 0
        stack = []
        for i in s:
            if i == '[':
                stack.append([res,n])
                res,n = "", 0
            elif i == ']':
                previous_res, cur_n = stack.pop()
                res = previous_res + cur_n*res
            elif '0' <= i <='9':
                n = n*10 + int(i   #乘以10是处理大于10的数
            else:
                res += i
        return res
                
