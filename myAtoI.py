class Solution:
    def myAtoi(self, str: str) -> int:

        new_str = str.replace(" ","")
        if len(new_str) == 0:
            return 0
        right_start = "-+0123456789"
        right_bottom = "0123456789"

        int_number = ""
        start_idx = -1
        if new_str[0] in right_bottom:
            signal = "+"
            if new_str[0] != "0":
                int_number += new_str[0]
                start_idx = 0
        elif new_str[0] not in right_start:
            return 0
        else:
            signal = new_str[0]
            start_idx = 1

        # number_minus = 0
        # signal = '+'
        if start_idx == -1:
            if len(new_str)>=2:
                for idx,value in enumerate(new_str[1:]):
                    if value in right_bottom:
                        if value != "0":
                            start_idx = idx
                            break
                    else:
                        return 0
            else:
                if int_number != "":
                    return int(int_number)
                else:
                    return 0

        if start_idx == -1:
            return 0

        flag = 0
        float_number = signal
        if int_number == "" : int_number = signal
        # int_number = signal
        #print(start_idx,float_number,int_number) #0 - -
        for i in new_str[start_idx:]:
            if flag == 0:
                if i == '.':
                    flag = 1
                    continue
                if i in right_bottom:
                    int_number = int_number + i
                else:
                    break
            else:
                float_number += i
        #print(int_number,float_number)
        if flag == 1:
            output = int(int(int_number)+int(float_number)/10**(len(float_number)-1))
        else:
               output = int(int_number)
        return output if -2147483648 < output < 2147483647 else -2147483648
test = Solution()
result = test.myAtoi("  -42")
print(result)