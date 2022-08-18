from collections import deque
import sys

# 13905(세부)문제랑 #1939(중량) 문제는 완전히 동일한 문제. 

def solve(s, e, graph, m):
    min_weight = 0 # 물품을 이 무게만큼 들고 있으면 반드시 배송 가능
    max_weight = m + 1 # 물품을 이 무게만큼 들고 있으면 절대 배송 불가능
    N = len(graph)
    while min_weight + 1 != max_weight:
        test_weight = (min_weight + max_weight) // 2
        visited = [False for _ in range(N)]
        queue = deque([s])
        success = False
        while queue:
            here = queue[0]
            queue.popleft()
            for there, weight in graph[here]:
                if visited[there]:
                    continue
                else:
                    if weight >= test_weight:
                        visited[there] = True
                        if there == e:
                            success = True
                            break
                        queue.append(there)
            if success:
                break
        if success:
            min_weight = test_weight
        else:
            max_weight = test_weight
    return min_weight

if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())
    graph = [[] for _ in range(N)]
    max_weight = 0
    s, e = map(int, read().split())
    s, e = s-1, e-1
    for i in range(M):
        A,B,C = map(int, read().split())
        graph[A-1].append((B-1, C))
        graph[B-1].append((A-1, C))
        max_weight = max(max_weight, C)
    print(solve(s, e, graph, max_weight))