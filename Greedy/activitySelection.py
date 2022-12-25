
class Activity :
    def __init__(self ,start : int, end : int) -> None:
        self.start = start
        self.end = end
        self.duration = self.end - self.start

    def __lt__(self , act ) :
        return self.start < act.start

    def __gt__(self , act) :
        return self.start > act.start
    


def solve(timelist : list) :

    timearr = [ 0 for i in range(25)]
    print(timelist)
    timelist.sort()
    print(timelist)
    

    for start,end in timelist :
        for i in range(start ,end) :
            timearr[i] +=1
        
    print(timearr)
    return max(timearr)


if __name__ == "__main__" :
    # timelist = [[1,3] , [2,4] , [3,8] , [10,11]]
    timelist = [[1,3] , [3,4] , [4,5] , [2,6] , [5,7] , [6,9]]
    print(solve(timelist))
