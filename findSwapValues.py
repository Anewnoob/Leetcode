#面试题 16.21. 交换和
#给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。
#返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。


class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        if not array1 or not array2:
            return []

        sum_a1 = 0
        sum_a2 = 0
        for i in array1:
            sum_a1 += i
        for j in array2:
            sum_a2 += j

        c = sum_a1-sum_a2
        if c%2 != 0:
            return []
        c = c//2
        array1 = set(array1)
        array2 = set(array2)
        
        for i in array1:
            if i - c in array2:
                return [i,i-c]
        return []
            
