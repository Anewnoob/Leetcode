class Solution:
    #暴力法
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len < 2 : return s

        #init
        max_len = 1
        max_subPalidrome = s[0]

        for i in range(s_len-1):
            for j in range(i+1,s_len):
                if j-i+1 > max_len:
                    #判断是否为回文
                    if self.isPalidrome(s[i:j+1]):
                        max_len = j-i+1
                        max_subPalidrome = s[i:j+1]
        return max_subPalidrome

    def isPalidrome(self, sub_string):
        start = 0
        end = len(sub_string) - 1
        while start < end:
            if sub_string[start] == sub_string[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
