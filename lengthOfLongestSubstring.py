class Solution:
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


test = Solution()
result = test.lengthOfLongestSubstring("cdd")
print(result)
