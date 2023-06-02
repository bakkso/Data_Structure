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


def get_10_11_matrix():
    # 정점 리스트 생성
    vertex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # 인접 행렬 초기화
    adjMat = [[0] * 10 for i in range(10)]

    # 간선 추가 함수 정의
    def add_edge(i: int, j: int):
        adjMat[i][j] = 1
        adjMat[j][i] = 1

    # 간선 추가
    add_edge(0, 1)
    add_edge(1, 2)
    add_edge(1, 3)
    add_edge(2, 4)
    add_edge(3, 4)
    add_edge(3, 5)
    add_edge(5, 6)
    add_edge(5, 7)
    add_edge(6, 7)
    add_edge(7, 8)
    add_edge(7, 9)

    # 정점 리스트와 인접 행렬 반환
    return vertex, adjMat


vertex, adjMat = get_10_11_matrix()

print('Spanning Tree(DFS) : ', end="")
st_dfs(adjMat, vertex, 0)
print()


# vtx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# adj = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
#        [0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
#        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
#        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
#        [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
#        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
