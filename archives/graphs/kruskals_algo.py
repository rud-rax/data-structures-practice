from graph import Graph


g = Graph()
g.addEdge(1, 6)
g.addEdge(1, 2)
g.addEdge(6, 5)
g.addEdge(5, 7)
# g.addEdge(7,2)
g.addEdge(2, 3)
g.addEdge(7, 4)

g.displayAdjList()
print(g.fromCycle())


# g = WeightedGraph()

# g.addEdge(1, 2, 28)
# g.addEdge(1, 6, 10)
# g.addEdge(2, 3, 16)
# g.addEdge(2, 7, 14)
# g.addEdge(6, 5, 25)
# g.addEdge(5, 7, 24)
# g.addEdge(4, 7, 18)
# g.addEdge(5, 4, 22)
# g.addEdge(4, 3, 12)

# g.displayAdjList()


# sorted_list = [[999999999, 9999999999, 9999999999]]


# for v1 in g.graph.keys():

#     for v2, cost in g.graph[v1]:

#         i = 0
#         # v2, cost = g.graph[v1][i]

#         if [min(v1, v2), max(v1, v2), cost] not in sorted_list:

#             while cost > sorted_list[i][2] and i < len(sorted_list):
#                 i += 1
#             sorted_list.insert(i, [min(v1, v2), max(v1, v2), cost])


# print(sorted_list := sorted_list[:-1])


# visited = []

# totalcost = 0

# i = 0


# i = 0
# while len(visited) <= len(g.graph.keys()) - 1 and i < len(sorted_list):

#     v1, v2, cost = sorted_list[i]

#     if [min(v1, v2), max(v1, v2), cost] not in visited:
#         totalcost += cost
#         visited.append([min(v1, v2), max(v1, v2), cost])

#     i += 1


# while len(visited) <= len(g.graph.keys()) - 1:
#     v1, v2, c = sorted_list[i]

#     if v1 not in visited or v2 not in visited:
#         totalcost += c
#         if v1 not in visited:
#             visited.append(v1)
#         if v2 not in visited:
#             visited.append(v2)

#     i += 1


# print(visited)
# print(totalcost)
