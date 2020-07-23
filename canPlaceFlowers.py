假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        flowerbed_len = len(flowerbed)
        flowerbed.insert(0,0)
        flowerbed.append(0)
        conut = 0
        for i in range(1,flowerbed_len+1):
            if flowerbed[i] + flowerbed[i-1] + flowerbed[i+1] == 0:
                flowerbed[i] = 1
                conut += 1
        return conut >= n
