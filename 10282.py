import sys
from queue import PriorityQueue as pq
def make_graph(N, D):
    '''
    D: 의존성 리스트 d[u] = [a_u, b_u, s_u]
    return: 그래프 return[u] = [(node, dist) for nodes near to node u]
    '''
    result = [[] for _ in range(N)]
    for a, b, s in D:
        result[b-1].append((a-1, s))
    return result

def solve(n, d, c):
    '''
    n: 컴퓨터 갯수
    d: 의존성 리스트 d[u] = [a_u, b_u, s_u]
    c: 해킹당한 컴퓨터 번호(1-index). dijkstra 시작점
    '''
    c = c - 1 # (0-index)
    #print(f"solve: {n} computers, start from {c+1}")
    INFTY = 10**9+1
    visited = [False for _ in range(n)]
    distance = [INFTY for _ in range(n)]
    result = [0, 0]
    graph = make_graph(n, d)
    queue = pq()
    queue.put((0, c))
    distance[c] = 0
    while not queue.empty():
        cost, here = queue.get()
        if visited[here]:
            continue
        
        visited[here] = True
        distance[here] = cost
        result[0] += 1
        result[1] = max(result[1], distance[here])

        #print(f"visited: node {here + 1} (1-index), cost= {distance[here]}")
        for there, dist in graph[here]:
            #print(f"\tShould I visit {there+1}..?, dist from here={dist}")
            if not visited[there]:
                new_dist = distance[here] + dist
                if new_dist < distance[there]:
                    #print(f"\tYes.")
                    queue.put((new_dist, there))
                #else:
                    #print(f"\tI already can visit there at cost {distance[there]}, {new_dist} is too much.")
            #else:
                #print(f"\tI already visited {there+1}.")
    return result

if __name__ == '__main__':
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        n, d, c = map(int, read().split())
        dependency = []
        for i in range(d):
            dependency.append(list(map(int, read().split())))
        p, q = solve(n, dependency, c)
        print(p, q)