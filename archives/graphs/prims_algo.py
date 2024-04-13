from graph import WeightedGraph


g = WeightedGraph()

g.addEdge(1, 2, 28)
g.addEdge(1, 6, 10)
g.addEdge(2, 3, 16)
g.addEdge(2, 7, 14)
g.addEdge(6, 5, 25)
g.addEdge(5, 7, 24)
g.addEdge(4, 7, 18)
g.addEdge(5, 4, 22)
g.addEdge(4, 3, 12)

g.displayAdjList()


# START
node = 1
nv = 7
cost = 0
path = [node]

for _ in range(1, nv):

    minn = 9999999999
    for i in range(0, len(g.graph[node])):
        if g.graph[node][i][1] < minn and g.graph[node][i][0] not in path:
            nextnode = g.graph[node][i][0]
            nextcost = g.graph[node][i][1]

    node = nextnode
    cost += nextcost
    path.append(node)


print(cost)
print(path)
