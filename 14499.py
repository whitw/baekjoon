import sys

def roll(N, M, x, y, dice, direction):
    #dice: 길이 6 배열. 문제 시작시점 기준 [2,4,1,3,5,6] 순
    #[북쪽 서쪽 윗면 동쪽 남쪽 바닥]
    #direction: int
    if direction == 1: #동으로 굴러
        if x != M - 1:
            return True, x+1, y, [dice[0], dice[5], dice[1], dice[2], dice[4], dice[3]]
        else:
            return False, x, y, dice
    elif direction == 2: #서로 굴러
        if x != 0:
            return True, x-1, y, [dice[0], dice[2], dice[3], dice[5], dice[4], dice[1]]
        else:
            return False, x, y, dice
    elif direction == 3: #북으로 굴러
        if y != 0:
            return True, x, y-1, [dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]]
        else:
            return False, x, y, dice
    else: #남으로 굴러
        if y != N - 1:
            return True, x, y+1, [dice[5], dice[1], dice[0], dice[3], dice[2], dice[4]]
        else:
            return False, x, y, dice
def solve(N, M, board, x, y, op):
    result = []
    dice = [0,0,0,0,0,0]
    for i in op:
        t, x, y, dice = roll(N, M, x, y, dice, i)
        if t:
            if board[y][x] == 0:
                board[y][x] = dice[5]
            else:
                dice[5] = board[y][x]
                board[y][x] = 0
            result.append(dice[2])
    return result



if __name__ == '__main__':
    read = sys.stdin.readline
    N, M, y, x, k = map(int, read().split())
    board = [[i for i in map(int,read().split())] for _ in range(N)]
    #print(board)
    op = [i for i in map(int, read().split())]
    firstOutput = True
    for i in solve(N, M, board, x, y, op):
        if firstOutput:
            print(str(i), end='')
            firstOutput = False
        else:
            print('\n' + str(i), end='')
    