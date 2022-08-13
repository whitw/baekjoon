import sys
from functools import cmp_to_key

def cmp(a, b):
    if a[1] == b[1]:
        return a[0] - b[0]
    return a[1] - b[1]

def process(arr, N):
    # 정렬해야 할 내용만, 1차원 리스트로 전달.
    # 정렬한 내용을 1차원 리스트로 반환.
    # 리스트를 해석하고 배열을 업데이트하는 것은 호출자의 몫으로 둔다.
    contains = {}
    #print(f"\tprocess received param:{arr[:N]}")
    for i in arr[:N]:
        if i in contains:
            contains[i] += 1
        else:
            contains[i] = 1
    contains.pop(0, None)
    items = sorted(contains.items(), key=cmp_to_key(cmp))
    #print(f"\tkey, value= {items}")
    result = []
    for i, j in items:
        result.append(i)
        result.append(j)
    #print(f"\tprocess returns result:{result}")
    return result

def solve(r,c,k,A):
    nrow = 3 #세로줄 갯수
    ncol = 3 #가로줄 갯수

    ntrow, ntcol = nrow, ncol
    for turn in range(101):
        if A[r][c] == k:
            return turn
        if nrow >= ncol:
            for i in range(nrow):
                newrow = process(A[i], ncol)
                for j in range(ncol):
                    A[i][j] = 0
                for j, val in enumerate(newrow):
                    if j >= 100:
                        break
                    A[i][j] = val
                    #print(f"A[{i}][{j}]={A[i][j]}")
                if ntcol < len(newrow):
                    ntcol = len(newrow)
        else:
            for i in range(ncol):
                newcol = process([A[j][i] for j in range(nrow)], nrow)
                for j in range(nrow):
                    A[j][i] = 0
                for j, val in enumerate(newcol):
                    if j >= 100:
                        break
                    A[j][i] = val
                    #print(f"A[{j}][{i}]={A[j][i]}")
                if ntrow < len(newcol):
                    ntrow = len(newcol)
        nrow, ncol = ntrow, ntcol
        
        #print(f"\nturn={turn}")
        #for i in range(nrow):
        #    for j in range(ncol):
        #        print(f"{A[i][j]:02d}", end=' ')
        #    print()
        
        if nrow > 100:
            nrow = 100
        if ncol > 100:
            ncol = 100

    return -1
    

if __name__ == '__main__':
    read = sys.stdin.readline
    r,c,k = map(int, read().split())
    A = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(3):
        A[i][0], A[i][1], A[i][2] = map(int, read().split())
    print(solve(r-1,c-1,k,A))