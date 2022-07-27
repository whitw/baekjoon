import sys
from collections import deque
up=0
right=2
down=4
left=6

def connected(t, idx):
    # 톱니바퀴 튜플 t에서 idx번째 톱니(0-idx)와 idx+1번째
    # 톱니가 함께 움직이는지 검사.
    # idx error 등은 전혀 체크하지 않는다. 그건 알아서 할것.
    if t[idx][right] != t[idx+1][left]:
        return True
    return False

def solve(t,op):
    for idx, direction in op:
        idx -= 1
        conn = [False] * 4
        dir = [0] * 4
        conn[idx] = True
        dir[idx] = direction
        for _ in range(3):
            for i in range(3):
               if connected(t, i):
                conn[i] = conn[i] or conn[i+1]
                conn[i+1] = conn[i] or conn[i+1]
        for i in range(4):
            if conn[i]:
                dir[i] = (-1) ** abs(i - idx) * direction
        #print('t=',t)
        #print('lr=', [(i[left],i[right]) for i in t])
        #print('idx,direction=',idx, direction)
        #print('conn,dir=',conn, dir)
        #print('')
        for i in range(4):
            if dir[i] == 1:
                t[i] = t[i][-1] + t[i][:-1]
            elif dir[i] == -1:
                t[i] = t[i][1:] + t[i][0]
    #print('t=', t)
    #print('u=', [i[up] for i in t])
    result = 0
    for i in range(4):
        result += int(t[i][up]) * (2 ** i)
    return result

if __name__ == '__main__':
    read = sys.stdin.readline
    t = [read().rstrip() for _ in range(4)]
    n_op = int(read())
    op = [tuple(map(int, read().split())) for _ in range(n_op)]
    print(solve(t, op))