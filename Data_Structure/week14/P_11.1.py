graphAL = {'A': set([('B', 29), ('F', 10)]),
           'B': set([('A', 29), ('C', 16), ('G', 15)]),
           'C': set([('B', 16), ('D', 12)]),
           'D': set([('C', 12), ('E', 22), ('G', 18)]),
           'E': set([('D', 22), ('F', 27), ('G', 25)]),
           'F': set([('A', 10), ('E', 27)]),
           'G': set([('B', 15), ('D', 18), ('E', 25)])}


def weightSum(graph):
    sum = 0
    for v in graph:
        for e in graph[v]:
            sum += e[1]
    return sum // 2


# def printAllEdges(graph):
#     temp = []
#     for v in graph:
#         for e in graph[v]:
#             if not e[1] in temp:
#                 print("(%s,%s,%d)" % (v, e[0], e[1]), end='')
#                 temp.append(e[1])

def printAllEdges(graph):
    temp = []
    for v in graph:
        for e in graph[v]:
            temp.append(e[1])
            if temp.count(e[1]) == 1:
                print("(%s,%s,%d)" % (v, e[0], e[1]), end='')


print('AL : weight sum = ', weightSum(graphAL))
printAllEdges(graphAL)
