import sys
from collections import deque

INF = 10000
dir = [(0,1), (1,0), (0,-1), (-1, 0)]

def solve(board, water, hedgehog):
    waterboard = [[INF for _ in  range(len(board[0]))] for _ in range(len(board))]
    hogboard = [[INF for _ in range(len(board[0]))] for _ in range(len(board))]
    result = "KAKTUS"
    queue = deque()
    for y, x in water:
        queue.append((y, x, 0))
        waterboard[y][x] = 0
    while queue:
        y, x, turn = queue[0]
        queue.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if (0 <= ny < len(board)) and (0 <= nx < len(board[0])):
                if waterboard[ny][nx] == INF and board[ny][nx] == '.':
                    waterboard[ny][nx] = turn + 1
                    queue.append((ny, nx, turn + 1))

    '''
    print("waterboard:")
    for i in waterboard:
        for j in i:
            if j == INF:
                print('I', end=' ')
            else:
                print(j, end=' ')
        print()
    '''
    queue = deque()
    queue.append((hedgehog[0], hedgehog[1], 0))
    while queue:
        y, x, hogturn = queue[0]
        #print(f"hog:{y, x, hogturn}")
        queue.popleft()
        if hogboard[y][x] != INF:
             continue
        hogboard[y][x] = hogturn
        #print(f"y,x,hogturn,board,water={y, x, hogturn,board[y][x], waterboard[y][x]}")

        if board[y][x] == 'D':
            result = str(hogturn)
            break
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                if hogturn + 1 < waterboard[ny][nx] and (board[ny][nx] == '.' or board[ny][nx] == 'D'):
                    queue.append((ny, nx, hogturn+1))
    '''
    print("hogboard:")
    for i in hogboard:
        for j in i:
            if j == INF:
                print('I', end=' ')
            else:
                print(j, end=' ')
        print()
    '''
    return result



if __name__ == '__main__':
    read = sys.stdin.readline
    R, C = map(int, read().split())
    board = []
    water = []
    hedgehog = None
    for i in range(R):
        board.append([j for j in read().rstrip()])
        for j, _ in enumerate(board[i]):
            if board[i][j] == 'S':
                hedgehog = (i, j)
            elif board[i][j] == '*':
                water.append((i, j))
    print(solve(board, water, hedgehog))
