import sys
from collections import deque

def solve(n, a, b, relation):
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for i, j in relation:
        graph[i].append(j)
        graph[j].append(i)
    queue = deque()
    queue.append((a, 0))
    visited[a] = True
    while queue:
        man, dist = queue[0]
        #print(f"man({man}), dist({dist})")
        queue.popleft()
        if man == b:
            return dist
        for i in graph[man]:
            #print(f"\tnear[{man}]={i}")
            if not visited[i]:
                visited[i] = True
                queue.append((i, dist + 1))
                #print(f"\tappend{i,dist + 1}")
    return -1

if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    a, b = map(int, read().split())
    m = int(read())
    relation = []
    for _ in range(m):
        r1, r2 = map(int, read().split())
        relation.append((r1 - 1, r2 - 1))
    print(solve(n, a - 1, b - 1, relation))