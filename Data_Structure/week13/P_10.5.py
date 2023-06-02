def toplogical_sort(graph):
    inDeg = {}
    for vtx in graph:
        inDeg[vtx] = 0

    # graph는 딕셔너리니까 len(graph)를 통해 길이를 구하는 것은 잘못된 방법
    # len(graph)는 그저 딕셔너리의 키의 개수를 반환함
    for i in graph:
        for j in graph[i]:
            inDeg[j] += 1

    vlist = []
    for i in graph:
        if inDeg[i] == 0:
            vlist.append(i)

    while len(vlist) > 0:
        v = vlist.pop()
        print(v, end=' ')

        for u in graph[v]:
            inDeg[u] -= 1
            if inDeg[u] == 0:
                vlist.append(u)


mygraph = {'2': {},
           '3': {'8', '10'},
           '5': {'11'},
           '7': {'8', '11'},
           '8': {'9'},
           '9': {},
           '10': {},
           '11': {'2', '9', '10'}
           }

print("toplogical_sort: ")
toplogical_sort(mygraph)
print()

# mygraph = {'A': {'C', 'D'},
#            'B': {'D', 'E'},
#            'C': {'D', 'F'},
#            'D': {'F'},
#            'E': {'F'},
#            'F': {}
#            }

# mygraph = [[0,0,0,0,0,0,0,0],
#            [0,0,0,0,1,0,0,1],
#            [0,0,0,0,0,0,0,1],
#            [0,0,0,0,1,0,0,1],
#            [0,0,0,0,0,0,0,0],
#            [0,0,0,0,0,1,0,0],
#            [0,0,0,0,0,0,0,0],
#            [1,0,0,0,0,1,0,1]]
