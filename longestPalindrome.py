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


class Solution2:
    """
    动态规划 :画一张 I*J的表格 进行填表  为回文的填true并记录位置 和长度  不是回文False
    """

    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]
    
    
        """
        中心扩散  考虑长度为奇数偶数的两种情况
        """
        size = len(s)
        if size < 2:
            return s

        # 至少是 1
        max_len = 1
        res = s[0]

        def center_spread(s, size, left, right):
            """
            left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
            right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
            """
            i,j = left,right
            while i >= 0 and j < size and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1:j], j - i - 1

        for i in range(size):
            palindrome_odd, odd_len = center_spread(s, size, i, i)
            palindrome_even, even_len = center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res


