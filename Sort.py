# including quickSort, mergeSort and headSort
#Sort

def quickSort(a,left,right):
    if left > right: return 
    tmp = a[left]
    i,j  = left,right
    while i < j:
        while i < j and a[j] >= tmp: j -= 1
        while i < j and a[i] <= tmp: i += 1
        if i < j:
            t = a[j]
            a[j] = a[i]
            a[i] = t
    #i = j
    a[left] = a[i]
    a[i] = tmp
    quickSort(a,left,i-1)
    quickSort(a,i+1,right)            

def merge(a,b):
    c = []
    len_a,len_b = len(a),len(b)
    i,j = 0,0
    while i < len_a and j < len_b:
        if a[i] <= b[j]: 
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len_a:
        c.append(a[i])
        i += 1
    while j < len_b:
        c.append(b[j])
        j += 1
    return c

def mergeSort(a):
    length = len(a)
    if length < 2: return a
    mid = length // 2
    return merge(mergeSort(a[:mid]),mergeSort(a[mid:]))


def headAdjust(a,parent,length):
    child = 2*parent+1  #左孩子
    while child < length:
        if child + 1 < length and a[child+1] > a[child]:
            child += 1
        if a[parent] >= a[child]: break
        #change
        h = a[parent]
        a[parent] = a[child]
        a[child] = h
        parent = child
        child = parent*2+1

def headSort(a):
    if not a: return a
    length = len(a)
    sort_a = a

    #最后一个节点得索引是(length // 2) -1
    #构造初始堆
    for i in range((length//2)-1,-1,-1):
        headAdjust(sort_a,i,length)
    
    #取顶堆元素并重新排序
    for j in range(length-1,0,-1):
        tmp = sort_a[j]
        sort_a[j] = sort_a[0]
        sort_a[0] = tmp

        #重新排序
        headAdjust(sort_a,0,j)
a = [2,3,1,4,8,5,6,9,7,10,11,19,15,4]
# quickSort(a,0,len(a)-1)
# print(a)

#res = mergeSort(a)
#print(res)

headSort(a)
print(a)

