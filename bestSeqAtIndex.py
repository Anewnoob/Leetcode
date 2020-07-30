有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        if not height or not weight: return 0
        hw = list(zip(height,weight))
        hw.sort(key = lambda x :(x[0],-x[1]))
        hw_len = len(hw)
        up_weight = [hw[0][1]]
        for i in range(1,hw_len):
            if up_weight[-1] < hw[i][1]:
                up_weight.append(hw[i][1])
            else:
                pos = bisect.bisect_right(up_weight,hw[i][1])
                if up_weight[pos-1] != hw[i][1]:
                    up_weight[pos] = hw[i][1]
        return len(up_weight)
