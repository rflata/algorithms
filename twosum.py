def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    """
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[(i+1):]):
            if n + m == target:
                return [i, j+i+1]
    """
    hashmap = {}
    for i, n in enumerate(nums):
        hashmap[n] = i
    for j, m in enumerate(nums):
        complement = target - m
        if hashmap.get(complement) != None:
            return [j, hashmap.get(complement)]
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))