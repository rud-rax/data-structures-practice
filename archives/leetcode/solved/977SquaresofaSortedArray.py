

def solve(nums) : 
    def partition(l , h ) :

        i = l
        for j in range(l + 1 , h + 1) :
            if nums[l] > nums[j] : 
                i+=1
                nums[i] , nums[j] = nums[j],nums[i]

        nums[l],nums[i] = nums[i],nums[l]

        return i

    def quickSort(l , h) :
        if l < h :
            i = partition(l , h )
            quickSort(l , i - 1)
            quickSort(i + 1 , h)
            
    nums = [x**2 for x in nums]

    quickSort(0 , len(nums) - 1)

    return nums


print(solve([-4,-1,0,3,10]))


    