409. 最长回文串
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s : return 0
        s_len = len(s)
        hashmap = {}
        max_len = 0
        for i in s:
            hashmap[i] = 0
        for i in s:
            hashmap[i] += 1
        flag = 0
        for val in hashmap.values():
            if val > 1:
                max_len += (val // 2)*2
            if val % 2 != 0 :
                flag = 1
        return max_len + flag
