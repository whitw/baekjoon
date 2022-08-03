from collections import deque

def solve(N, K):
    checked = [False for _ in range(100001)]
    queue = deque([(N, 0)])
    while queue:
        item = queue[0]
        queue.popleft()
        if not checked[item[0]]:
            checked[item[0]] = True
        else:
            continue
        if item[0] == K:
            return item[1]
        else:
            if(item[0] <= 50000):
                queue.append((item[0] * 2, item[1]+1))
            if(item[0] > 0):
                queue.append((item[0]-1, item[1]+1))
            if(item[0] < 100000):
                queue.append((item[0]+1, item[1]+1))

if __name__ == '__main__':
    N, K = map(int,input().split())
    print(solve(N, K))