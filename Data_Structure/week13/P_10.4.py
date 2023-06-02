def st_dfs_recur(adj, vtx, visited, id):
    visited[id] = True
    for i in range(len(vtx)):
        if visited[i] == False and adj[id][i] == 1:
            print("(", vtx[id], ",", vtx[i], ") ", end="")
            st_dfs_recur(adj, vtx, visited, i)


def st_dfs(adj, vtx, s):
    n = len(vtx)
    visited = [False]*n
    st_dfs_recur(adj, vtx, visited, s)
    return


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

print('Spanning Tree(DFS) : ', end="")
st_dfs(adj, vtx, 0)
print()
