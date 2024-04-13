

def solve(nums) :
    c = 0 
    i = 0 
    while i < len(nums) - c:
        if nums[i] == 0 :
            c +=1
            nums = nums[:i] + nums[i+1 : ] + [0]
            i-=1

        i+=1
        #     c +=1
        #     nums.pop(i)
        #     i-=1
        # i+=1

    # nums.extend([0]*c)
    
    return nums


nums = [0,1,0,3,12]
nums = solve(nums)
print(nums)