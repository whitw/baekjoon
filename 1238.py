import sys
from queue import PriorityQueue as pq

def dbg_print(*args, **kwargs):
    pass
    #print(*args, **kwargs)

def make_graph(N, edges, inverse=False):
    graph = [[] for _ in range(N)]
    if not inverse:
        for begin, end, dist in edges:
            graph[begin - 1].append((end-1, dist))
    else:
        for end, begin, dist in edges:
            graph[begin - 1].append((end-1, dist))
    return graph

def dijkstra(N, graph, start, INFTY=10**9+1):
    dbg_print(f"\tdijkstra({N}, {graph}, {start}) called")
    visited = [False for _ in range(N)]
    distance = [INFTY for _ in range(N)]
    queue = pq()
    queue.put((0, start))
    while not queue.empty():
        cost, here = queue.get()
        if visited[here]:
            continue
        dbg_print(f"\tVisited {here} with cost={cost}")
        visited[here] = True
        distance[here] = cost
        dbg_print(f"\tdistance updated\n\t{distance}\n\n")
        for there, length in graph[here]:
            dbg_print(f"\tShould I go {there} with length from here={length}?")
            if not visited[there]:
                if cost + length < distance[there]:
                    queue.put((cost+length, there))
                    dbg_print(f"\tYes.")
                else:
                    dbg_print(f"\tI can visit there in {cost+length} step. No.")
            else:
                dbg_print(f"\tNo. I already visited there.")
    return distance


def solve(N, edges, X):
    X = X - 1 #convert 1-indexed index to 0-index
    graph = make_graph(N, edges, inverse=False)
    inv_graph = make_graph(N, edges, inverse=True)
    dist = dijkstra(N, graph, X)
    inv_dist = dijkstra(N, inv_graph, X)
    result = -1
    for i in range(N):
        if dist[i] + inv_dist[i] > result:
            result = dist[i] + inv_dist[i]
    return result

if __name__ == '__main__':
    read = sys.stdin.readline
    N, M, X = map(int, read().split())
    edges = [list(map(int,read().split())) for _ in range(M)]
    print(solve(N, edges, X))

        
