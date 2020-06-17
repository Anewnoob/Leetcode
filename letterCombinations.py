#给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母
#输入："23"
#输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_len = len(digits)
        if digits_len == 0: return []
        hashmap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        product=['']
        for k in digits:
            product=[i+j for i in product for j in hashmap[k]]
        return product

