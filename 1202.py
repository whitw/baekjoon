import sys
from queue import PriorityQueue

def solve(MV, C):
    '''
    아이디어 정리
    C가 작은 가방부터 하나씩 순회할 것이다.
    보석은 V가 큰 것부터 꺼내야 하는데, 최소한 가방에는 들어갈 수 있는 크기여야 한다.
    각각을 미리 정렬해두고? C는 정렬 필요. MV는 M기준으로 집어넣고 V기준으로 선택해야 되니까
    마찬가지로 M기준으로 정렬해야 한다. V를 선택하기 위해 priority queue이용.
    '''
    C = sorted(C)
    MV = sorted(MV, key=lambda x: x[0])
    result = 0
    #print(C, MV)
    mvidx = 0
    pq = PriorityQueue()
    for c in C:
        while(mvidx < len(MV) and MV[mvidx][0] <= c):
            pq.put((-MV[mvidx][1], MV[mvidx]))
            #print("inserted MV[mvidx]=", MV[mvidx])
            mvidx += 1
        if not pq.empty():
            item = pq.get()[1]
            #print("popped item=",item)
            result += item[1]
        else:
            #print("pq is empty")
            pass
    return result


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    MV = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
    C = [int(sys.stdin.readline()) for _ in range(K)]
    #print(MV, C)
    print(solve(MV, C))
