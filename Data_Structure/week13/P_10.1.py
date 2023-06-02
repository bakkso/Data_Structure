def dfs_recur(adj, vtx, visited, id):
    print(vtx[id], end=' ')
    visited[id] = True
    for i in range(len(adj[id])):
        if visited[i] == False and adj[id][i] == 1:
            dfs_recur(adj, vtx, visited, i)


def dfs(adj, vtx, start):
    n = len(vtx)
    visited = [False] * n
    dfs_recur(adj, vtx, visited, start)


vtx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
adj = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]


print('DFS:', end=' ')
dfs(adj, vtx, 0)
print()


# vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# adj = [[0, 1, 1, 0, 0, 0, 0, 0],
#        [1, 0, 0, 1, 0, 0, 0, 0],
#        [1, 0, 0, 1, 1, 0, 0, 0],
#        [0, 1, 1, 0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0, 0, 1, 1],
#        [0, 0, 0, 1, 0, 0, 0, 0],
#        [0, 0, 0, 0, 1, 0, 0, 1],
#        [0, 0, 0, 0, 1, 0, 1, 0]]
