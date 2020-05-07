
#快排
def quickSort(a,left,right):
    if left >= right:
        return
    temp = a[left]
    i = left
    j = right
    while i < j:
        while a[j] >= temp and i < j:
            j -= 1
        while a[i] <= temp and i < j:
            i += 1
        if i < j:
            t = a[i]
            a[i] = a[j]
            a[j] = t
            print(a)

    a[left] = a[i]
    a[i] = temp
    quickSort(a,left,i-1)
    quickSort(a,i+1,right) 

a = [4,5,1,2,8,5,1,2,7,3,6,4,8,9,10,2,6,1,8]
quickSort(a,0,len(a)-1)
print(a)
