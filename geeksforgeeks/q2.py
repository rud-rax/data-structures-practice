

# def TotalPairs( nums, x, y):
#     c = 0 
#     for i in range(len(nums)) :
#         for j in range( i+1 , len(nums)) :
#             if x <= nums[i]*nums[j] <= y :
#                 c +=1
#     return c

def TotalPairs(nums, x, y) :

    c = 0 
    nums = sorted(nums)
    i = 0 
    

    while i < len(nums) :
        j = i +1 
        while j < len(nums) :
            j+=1
            if x <= nums[i]*nums[j] <= y :
                c+=1

            elif nums[i]*nums[j] > y:
                break
        i+=1
    return c


if __name__ == "__main__" :
    print("TESTCASE 1 = " , TotalPairs((5,3,7,9,7,9,7,7),7,19))
    print("TESTCASE 2 = " , TotalPairs((3,5,5,2,6),8,13))

