import sys
from collections import deque
from time import time

INF = 10000000
dir = ((1,0), (0,1), (-1,0), (0,-1))

def solve(board):
    N, M = len(board), len(board[0])
    DP = [[[INF] * 2 for _ in range(M)] for _ in range(N)]
    DP[0][0][0] = 1
    queue = deque()
    queue.append((0,0,0))
    while queue:
        y, x, w = queue[0]
        queue.popleft()
        #print(f"near(board,{(y,x,w)})={near(board,(y,x,w))}")
        oldcost = DP[y][x][w]
        if y == N-1 and w == M-1:
            return oldcost
        
        for i in dir:
            ny = y + i[0]
            nx = x + i[1]
            if nx < 0 or ny < 0 or ny >= len(board) or nx >= len(board[0]):
                continue
            if w == 1 and board[y][x] == 0:
                nw = 1
            elif w == 0:
                nw = board[y][x]
            else:
                continue
            if DP[ny][nx][nw] == INF:
                DP[ny][nx][nw] = oldcost + 1
                queue.append((ny,nx,nw))
                #print(f"append({ny, nx, nw})")
    #for i in DP:
    #    for j in i:
    #        print(j, end=' ')
    #    print()
    ans = min(DP[N-1][M-1][0], DP[N-1][M-1][1])
    if ans == INF:
        ans = -1
    return ans

if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = []
    for i in range(N):
        board.append([int(i) for i in read().rstrip()])
    #board = [[0 for i in range(1000)] for i in range(1000)]
    #t1 = time()
    print(solve(board))
    #t2 = time()
    #print(t2 - t1)