import queue


def isValidPos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'


def BFS():
    Q = queue.Queue(maxsize=0)
    Q.put((0, 1))
    print("BFS: ")

    while not Q.qsize() == 0:
        here = Q.get()
        print(here, end="->")
        x, y = here
        if(map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1):
                Q.put((x, y - 1))
            if isValidPos(x, y + 1):
                Q.put((x, y + 1))
            if isValidPos(x - 1, y):
                Q.put((x - 1, y))
            if isValidPos(x + 1, y):
                Q.put((x + 1, y))
    return False


map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '1', '0', '0', '1'],
       ['1', '0', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '0', '1', '0', '0', 'x'],
       ['1', '1', '1', '1', '1', '1']]
MAZE_SIZE = 6
result = BFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')
