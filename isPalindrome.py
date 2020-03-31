class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        str_len = len(str_x)
        if str_len <= 2 : return True
        head = 0
        tail = str_len -1
        while head < tail :
            if str_x[head] == str_x[tail]:
                head+=1
                tail-=1
            else:
                return False
        return True