import re


def findDistinctYears(input1) :
    
    pattern = " [\d]{2}-[\d]{2}-[\d]{4}"
    ed= 0
    c = []
    ma = re.search(pattern , input1[ed:] )
    while ma  :
        ed += ma.span()[1]
        c.append(input1[ed-4 : ed])
        ma = re.search(pattern , input1[ed:] )
        
    return len(set(c))

    
    
    
if __name__ == "__main__" :
    print(findDistinctYears('UN was established on 24-10-1945. India got freedom in 15-08-1940'))
    print(findDistinctYears('UN was established on 24-10-1945. India got freedom in 15-08-1945'))
    print(findDistinctYears('UN was established on 24-5. India got freedom in'))
    
    
    
    
