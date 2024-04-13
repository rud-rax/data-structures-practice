def twoSum( nums, target: int):
    
    for k,v in enumerate(nums) :
        r = target - v

        if r in nums and nums.index(r) != k :
            return [k,nums.index(r)]
        
print(twoSum(nums = [3,3] , target = 6))