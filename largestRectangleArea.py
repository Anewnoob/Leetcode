#给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。求在该柱状图中，能够勾勒出来的矩形的最大面积。

class Solution:
    #超出时间限制  固定高 ，变化宽
    def largestRectangleArea(self, heights: List[int]) -> int:
        # if not heights: return
        # list_len = len(heights)
        # max_val = 0
        # for i in range(list_len):
        #     left,right = i,i
        #     center_val = heights[i]
        #     #find left
        #     while i > 0 and heights[i-1] >= center_val:
        #         left -= 1
        #     #find right
        #     while i < list_len-1 and heights[i+1] >= center_val:
        #         right += 1
        #     #compute area
        #     area = heights[i] * (right-left-1)
        #     max_val = max(area,max_val)
        # return max_val

        #单调栈
        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        
        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)
        
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
