
arr1 = [10,15,20,50]
arr2 = [5,6,6,9,30,35]

res = []


i = 0
j = 0 

while i < len(arr1) and j < len(arr2) :
    if arr1[i] < arr2[j] :
        res.append(arr1[i])
        i +=1
    else :
        res.append(arr2[j])
        j+=1

if i == len(arr1) : 
    for ele in arr2[j : ] :
        res.append(ele)

if j == len(arr2) :
    for ele in arr1[i : ] :
        res.append(ele)

print(res)

