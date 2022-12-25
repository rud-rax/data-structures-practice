
def BFSDisconnected(adjlist) :

    visited = [False]*len(adjlist)

    for vertex in adjlist :
        if not visited[vertex] :
            BFS(adjlist , visited , start = vertex)
            
        



def BFS(adjlist , visited , start = 0, stop = None  ) :
    

    queue = [start]
    visited[start] = True
    while queue :
        curr = queue.pop(0)
        
        print(f"{curr} -> ",end = "")
        if curr == stop : 
            break
        for vertex in adjlist[curr] : 
            if visited[vertex] == False:
                queue.append(vertex)
                visited[vertex] = True


if __name__ == "__main__" :
    adjlist = [
        [1,2],
        [0,2,3],
        [0,1,3,4],
        [1,2,4],
        [2,3]
    ]
    BFS(adjlist , 0 )
        

