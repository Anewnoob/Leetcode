#给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
#找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#说明：你不能倾斜容器，且 n 的值至少为 2。


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # #暴力法
        # len_height = len(height)
        # if len_height < 2: return 0
        # max_area = 0
        # for left in range(len_height-1):
        #     for right in range(len_height-1,left,-1):
        #         if right < len_height-1 and height[right] <= height[right+1]:continue
        #         max_height = min(height[left],height[right])
        #         tmp = 0
        #         total_area = max_height*(right-left)#-tmp
        #         max_area = total_area if total_area > max_area else max_area
                
        # return max_area

        #双指针
        len_height = len(height)
        if len_height < 2: return 0
        max_area = 0
        left,right = 0,len_height-1
        while left < right:
            min_height = min(height[left],height[right])
            max_area = max(min_height*(right-left),max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


