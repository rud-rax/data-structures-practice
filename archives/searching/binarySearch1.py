

def binarySearch(nums , target) :
    
    l = 0
    h = len(nums) - 1
    
    while l <= h :
        
        mid = (l + h) // 2
        
        if nums[mid] == target :
            return target
        elif nums[mid] > target :
            h = mid - 1
        else :
            l = mid + 1
            
    return -1
    
    
print(binarySearch(nums = [-1,0,3,5,9,12], target = 9))