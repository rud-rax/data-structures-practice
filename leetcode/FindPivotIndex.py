



def solve(nums) :
    # print(nums)
    
    i = 0 
    j = len(nums) - 1
    
    ls = 0 
    rs = 0 
    
    if nums[i] < nums[j] :
        ls+=nums[i]
        i+=1
    else :
        rs+= nums[j]
        j-=1
    
    while i < j :
        if ls < rs :
            ls+=nums[i]
            i+=1
        else  :
            rs += nums[j]
            j -=1
            
    if ls == rs and i == j:
        return i
    return -1
            
        
def solve1(nums) :
    ls = 0 
    rs = sum(nums) 
    for i in range(len(nums)) :
        
        rs -= nums[i]
        
        if ls == rs :
            return i
        
        ls += nums[i]
    return -1 


if __name__ == "__main__" :
    print(solve1([1,7,3,6,5,6]))
    # solve1([1,2,3])
    # solve1([2,1,-1])
    