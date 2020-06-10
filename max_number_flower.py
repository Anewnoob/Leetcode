#求能够种值得新的花数量  要求，原花得两边不能种植花
def max_number_flower(n,a):
    if not a: return 
    length = len(a)
    pre_num = 0
    for val in a:
        if val == 1:
            pre_num += 1
    if length <= 2 and pre_num == 0: return 1
    
    b = [0]
    for val in a:
        b.append(val)
    b.append(0)
    
    num = 0
    i,j,k = 0,1,2
    for _ in b[1:-1]:
        if b[j] == 0:
            if b[i] == 0 and b[k] == 0:
                del b[j]
                b.insert(j,1)
                num += 1
        i += 1
        j += 1
        k += 1
    return num

n = 5
a = [1,0]
res = max_number_flower(n,a)
print(res)
