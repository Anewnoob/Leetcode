"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
class Solution:
    #暴力法
    def lengthOfLongestSubstring(self, s: str) -> int:
        total_lenth = len(s)
        if total_lenth == 0:
            return 0
        if total_lenth == 1:
            return 1
        max_len = 0
        for i in range(total_lenth):
            sub_string = ""
            sub_string = sub_string + s[i]


            if max_len >=total_lenth - i:
                return max_len

            if i  == total_lenth -2:
                if s[i+1] in sub_string:
                    return len(sub_string)
                else:
                    return len(sub_string)+1

            for j in range(i+1,total_lenth):
                if s[j] not in sub_string:
                    sub_string = sub_string + s[j]

                else:
                    current_max = len(sub_string)
                    if current_max > max_len:
                        max_len = current_max
                    break
                if len(sub_string) > max_len:
                    max_len = len(sub_string)
    #滑动窗口-- 类似蚯蚓前进
    def lengthOfLongestSubstringv2(self, s: str) -> int:
        class Solution:
            def lengthOfLongestSubstring(self, s: str) -> int:
                if not s:
                    return 0
                left = 0
                lookup = set()
                n = len(s)
                max_len = 0
                cur_len = 0
                for i in range(n):
                    cur_len += 1
                    while s[i] in lookup:
                        lookup.remove(s[left])
                        left += 1
                        cur_len -= 1
                    if cur_len > max_len:
                        max_len = cur_len
                    lookup.add(s[i])
                return max_len

test = Solution()
result = test.lengthOfLongestSubstring("cdd")
print(result)
