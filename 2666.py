import sys
from collections import deque
import time

INF = 200

def get_near(N, state):
    a, b = state
    result = []
    if a > 0:
        result.append((a-1, b))
    if a+1 < b:
        result.append((a+1, b))
        result.append((a, b-1))
    if b < N-1:
        result.append((a, b+1))
    return result

def solve(N, state, doors):
    # 그래프 이론으로 접근,
    # 각 노드는 (열린 문1, 열린문2(*오름차순))으로 나타내며
    # 각 상태에서 한번의 문 이동으로 다음 상태로 넘어갈 수 있다면
    # 엣지로 해석
    # fastest[(i,j)][k]:
    # k번째 문까지 연 채 노드(i,j)까지 올 수 있는 가장 빠른 시간,
    # 첫 상태가 (2, 5)라면 fastest[(2,5)][0] = 0, 나머지는 무한이 된다.
    # 이후 (3, 5)로 이동해 문 하나를 열었다면
    # fastest[(3,5)][1] = 1이 된다.
    fastest = {}
    for i in range(N):
        for j in range(i, N):
            fastest[(i,j)] = [INF for _ in range(len(doors) + 1)]
    if doors[0] in state:
        queue = deque([(state, 1)])
        fastest[state][1] = 0
    else:
        queue = deque([(state, 0)])
        fastest[state][0] = 0
        #print(f"queue.append({queue[0]})")
    while(queue):
        state, k = queue[0]
        queue.popleft()
        if k == len(doors):
            return fastest[state][k]
        near = get_near(N, state)
        for next in near:
            #print(f"test for next:{next}")
            if doors[k] in next:
                nk = k + 1
                if k+1 < len(doors) and doors[k+1] in next:
                    nk = k + 2
            else:
                nk = k
            if fastest[next][nk] > fastest[state][k] + 1:
                #print(f"dp[{next}][{nk}] update, {fastest[next][nk]} -> {fastest[state][k] + 1}")
                fastest[next][nk] = fastest[state][k] + 1
                queue.append((next, nk))
                #print(f"queue.append({next}, {nk})")

if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    s1, s2 = map(int, read().split())
    state = (s1-1, s2-1)
    n_door = int(read())
    doors = []
    for _ in range(n_door):
        doors.append(int(read()) - 1)
    #print(f"solve: {N}, {state}, {doors}")
    start = time.time()
    print(solve(N, state, doors))
    end = time.time()
    #print("time: ", end-start)