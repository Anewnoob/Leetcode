def fn(a,wordDict):
    if not a: return True

    a_len = len(a)
    dp = [False]*(a_len+1)
    dp[0] = True

    for i in range(1,a_len+1):
        for j in range(i):
            if dp[j] and a[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]


a = "todayisagooddayb"
wordDict = ["today","is","a","good","day"]
res = fn(a,wordDict)
print(res)

