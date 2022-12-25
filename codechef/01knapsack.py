


val = [60, 100, 120]
wt = [10, 20, 30]
n = len(wt)
W = 50 # total capacity

V = [[0 for x in range(W + 1)] for x in range(n + 1)]


for i in range(1 , n+1) : # till 4
    for w in range(1 , W + 1) : # till 51
        if wt[i - 1] <= w : 
            V[i][w] = max(V[i-1][w] , V[i-1][w - wt[i-1]] + val[i-1])
        
        else :
            V[i][w] = V[i-1][w]
            
V
            

        
    