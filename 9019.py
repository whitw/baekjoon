import sys
from collections import deque

def solve(A, B):
    queue = deque()
    prevNode = [None] * 10000
    prevOperation = [None] * 10000
    queue.append(A)
    if A == B:
        return ''

    while queue:
        item = queue[0]
        queue.popleft()

        if item == B:
            node = prevNode[B]
            result = prevOperation[B]
            while(node != A):
                result = prevOperation[node] + result
                node = prevNode[node]
            return result

        next = [((item * 2) % 10000, 'D'),
                ((item + 9999) % 10000, 'S'),
                ((item * 10) % 10000 + item // 1000, 'L'),
                ((item // 10) + 1000 * (item % 10), 'R')
                ]

        for nextNode, nextOperation in next:
            if prevOperation[nextNode] == None:
                prevNode[nextNode] = item
                prevOperation[nextNode] = nextOperation
                queue.append(nextNode)

if __name__ == '__main__':
    read = sys.stdin.readline
    T = int(read())
    for i in range(T):
        A,B = map(int, read().split())
        print(solve(A, B))