#哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写##之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

#注意：本题相对原题稍作改动，只需返回未识别的字符数


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if sentence == "": return 0
        s_len = len(sentence)
        dp = [0] * (s_len+1)
        for i in range(1,s_len+1):
            dp[i] = dp[i-1] + 1
            for j in range(i):
                if sentence[j:i] in dictionary:
                    dp[i] = dp[j] if dp[j] < dp[i] else dp[i]
        return dp[-1]
                
