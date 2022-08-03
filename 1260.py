import sys
from collections import deque
def dfs(N, graph, V):
    visited = [False for i in range(N)]
    result = []
    stack = deque()
    stack.append(V)
    while stack:
        node = stack[-1]
        stack.pop()
        if visited[node] == False:
            visited[node] = True
            result.append(node)
            for i in graph[node][::-1]:
                stack.append(i)
    return result


def bfs(N, graph, V):
    visited = [False for i in range(N)]
    result = []
    queue = deque()
    queue.append(V)
    while queue:
        node = queue[0]
        queue.popleft()
        if visited[node] == False:
            visited[node] = True
            result.append(node)
            for i in graph[node]:
                queue.append(i)
    return result

def solve(N, graph, V):
    '''
    그래프 구조 먼저 정의
    graph[i]: 노드 i에 연결된 노드들의 리스트
    0-1-3-4-2 형태로 이루어진 그래프라면
    graph:
    [0]:[1]
    [1]:[0,3]
    [2]:[4]
    [3]:[1,4]
    [4]:[2,3]
    형태로 저장된다.
    '''
    return (dfs(N,graph, V), bfs(N, graph, V))


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M, V = map(int,read().split())
    V -= 1
    graph = [[] for _ in range(N)]
    for i in range(M):
        begin, end = map(int, read().split())
        assert(begin != end)
        begin -= 1
        end -= 1
        graph[begin].append(end)
        graph[end].append(begin)
    for i in range(N):
        graph[i] = sorted(graph[i])
    ds, bs = solve(N, graph, V)
    print(' '.join([str(i+1) for i in ds]))
    print(' '.join([str(i+1) for i in bs]))
