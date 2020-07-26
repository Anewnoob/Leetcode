编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        """DP"""
        # dp = [0] * n
        # pointer = [0] * len(primes)
        # dp[0] = 1
        # for i in range(1, n):
        #     dp[i] = min(x * dp[y] for x, y in zip(primes, pointer))
        #     for j in range(len(primes)):
        #         if dp[i] == primes[j] * dp[pointer[j]]:
        #             pointer[j] += 1
        # return dp[-1]

        """heap"""
        heap = []
        heapq.heappush(heap,1)

        queue = set()
        queue.add(1)

        for i in range(n):
            cur_prime = heapq.heappop(heap)
            for p in primes:
                new_prime = cur_prime * p
                if new_prime not in queue:
                    queue.add(new_prime)
                    heapq.heappush(heap,new_prime)
        return cur_prime
        
