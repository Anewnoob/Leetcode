实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)

        if not haystack and not needle: return 0
        if not haystack: return -1
        if not needle: return 0
        i, j =0 ,0
        start = 0
        while i < h_len and j < n_len:
            i = start
            if h_len - start < n_len:
                return -1
            while i < h_len and j < n_len:
                if haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    start += 1
                    j = 0
                    break
            if j == n_len: return start

        #better
        for i in range(h_len):
            if i+n_len < h_len+1 and haystack[i:i+n_len] == needle:
                return i
        return -1
