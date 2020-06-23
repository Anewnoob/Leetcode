#给你两个二进制字符串，返回它们的和（用二进制表示）。
#输入为 非空 字符串且只包含数字 1 和 0。

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0': return b 
        if b == '0': return a

        len_a = len(a)
        len_b = len(b)
        min_len = min(len_a,len_b)
        flag = 0
        
        i,j = len_a-1,len_b-1
        res = ""
        for _ in range(min_len):
            tmp = int(a[i])+int(b[j])+flag
            if tmp >= 2: 
                flag = 1
                tmp = tmp - 2
            else:
                flag = 0
            res = str(tmp) + res
            i -= 1
            j -= 1
        
        if len_a == len_b:
            if flag == 0: 
                return res
            else:
                return '1' + res 

        if len_a >len_b:
            pre = a[:len_a-len_b]
        else:
            pre = b[:len_b-len_a]
        if flag == 0:
            return pre+res
        else:
            k = len(pre)
            print(k)
            for _ in range(k):
                tmp = int(pre[k-1])+flag
                if tmp >= 2:
                    flag = 1
                    tmp = tmp - 2
                else:
                    flag = 0
                res = str(tmp) + res
                k -= 1
        if flag == 0: 
            return res
        else:
            return '1' + res 
