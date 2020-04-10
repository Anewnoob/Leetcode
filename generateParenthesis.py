class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #DFS METHOD
        Parenthesis_list = []
        singleParenthesis = ""
        def dfs_method(singleParenthesis,left_num,right_num):
            #left_num:左括号剩余数量 right_num:右括号剩余数量
            if left_num == 0 and right_num == 0:
                Parenthesis_list.append(singleParenthesis)
                return
            if left_num > right_num:
                return
            if left_num > 0:
                dfs_method(singleParenthesis+'(',left_num-1,right_num)
            if right_num > 0:
                dfs_method(singleParenthesis+')',left_num,right_num-1)
        dfs_method(singleParenthesis,n,n)
        return Parenthesis_list
        
        
    #DP 动态规划
    def generateParenthesis_v1(self, n: int) -> List[str]:
        if n == 0:
            return []

        dp = [None for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for s1 in left:
                    for s2 in right:
                        cur.append("(" + s1 + ")" + s2)
            dp[i] = cur
        return dp[n]

