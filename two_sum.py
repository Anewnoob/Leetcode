def twoSum(nums, target):
    hashmap={}
    #construct hash map
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    #  if target -num in hashmap, then output the index
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]