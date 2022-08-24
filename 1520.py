import sys


def solve(N, M, board):
    DP = [[-1 for _ in range(M)] for _ in range(N)]
    DP[0][0] = 1
    def get(y, x):
        dy = [ 1,-1, 0, 0]
        dx = [ 0, 0, 1,-1]
        if DP[y][x] == -1:
            result = 0
            for i in range(4):
                ny,nx = y+dy[i], x+dx[i]
                #print(f"({y}, {x}): trying ({ny}, {nx})...")
                if (0 <= ny < N) and (0 <= nx < M) and (board[ny][nx] > board[y][x]):
                    #print(f"call ({y},{x}) += ({ny}, {nx})")
                    result += get(ny, nx)
            #print(f"get({y}, {x}) = {result} (recurse)")
            DP[y][x] = result
            return result
        else:
            #print(f"get({y}, {x}) = {DP[y][x]} (given)")
            return DP[y][x]
    result = get(N-1, M-1)
    if result == -1:
        return 0
    return result

if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [list(map(int, read().split())) for _ in range(N)]
    print(solve(N, M, board))
