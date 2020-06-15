#编写一个函数来查找字符串数组中的最长公共前缀。

#如果不存在公共前缀，返回空字符串 ""。

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre_fix = ""
        if not strs: return pre_fix
        len_strs = len(strs)

        for j in range(len(strs[0])):
            cur_letter = strs[0][j]
            for i in range(1,len_strs):
                word_len = len(strs[i])
                if j >= word_len:
                    return pre_fix
                if strs[i][j] != cur_letter:
                    return pre_fix
            pre_fix += cur_letter
        return pre_fix
            
            
