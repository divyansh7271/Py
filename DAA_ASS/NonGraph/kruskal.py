def find(i, parent):
    if i == parent[i]:
        return i
    return find(parent[i], parent)

def union(parent, rank, x, y):
    xroot = find(x, parent)
    yroot = find(y, parent)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph, V):
    i = 0
    e = 0
    parent = []
    rank = []
    result = []

    graph = sorted(graph, key = lambda item : item[2])

    for node in range(V):
        parent.append(node)
        rank.append(0)

    while e < (V - 1):
        u, v, w = graph[i]
        i = i + 1

        x = find(u, parent)
        y = find(v, parent)

        if x != y:
            result.append([u, v, w])
            e = e + 1
            union(parent, rank, u, v)

    minimumcost = 0
    for u, v, w in result:
        minimumcost += w
        print(u, ' -> ', v, ' : ', w)

    print('Minimum cost of the spanning tree = ',minimumcost)


graph = []
V = 4
graph.append([0,1,10])
graph.append([0,2,6])
graph.append([0,3,5])
graph.append([1,3,15])
graph.append([2,3,4])
print(f'The graph is: {graph}')
kruskal(graph, V)