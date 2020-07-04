#给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#有效字符串需满足：
#左括号必须用相同类型的右括号闭合。
#左括号必须以正确的顺序闭合。
#注意空字符串可被认为是有效字符串。


class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        s_len = len(s)
        stack = ["*"]
        haspmap = {'(':')','[':']','{':'}'}
        for i in range(s_len):
            if s[i] in "({[":
                stack.append(s[i])
            elif s[i] in ")}]":
                left = stack.pop()
                if left == '*': return False
                if haspmap[left] != s[i]: return False
            else:
                pass
        if len(stack)>1: return False
        return True
        
