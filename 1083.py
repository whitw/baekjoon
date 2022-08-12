import sys

def solve(arr, S):
    remain = S
    for j in range(0, len(arr) - 1):
        '''
        남은 횟수를 최대한 써서 가장 큰 값을 최대한 앞으로 옮겨야 한다.
        bubble sort처럼 접근했는데, 그게 아니라 selection sort처럼
        접근해야 할 것 같다.
        '''
        maxval = 0
        maxvalidx = 0
        #print(f"eoarr={min(len(arr), j+remain)}")
        for i, val in enumerate(arr[j:min(len(arr)-1, j+remain) + 1]):
            #print(f"i({i}),val({val})")
            if val > maxval:
                maxval, maxvalidx = val, i+j
        #print(f"arr[{maxvalidx}]={maxval}")
        for i in range(maxvalidx, j, -1):
            #print(f"i={i}")
            if arr[i] > arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                #print(f"{remain:02d}:{arr}")
                remain -= 1
    return arr

if __name__ == '__main__':
    read = sys.stdin.readline
    read()
    arr = list(map(int, read().split()))
    S = int(read())
    print(' '.join([str(i) for i in solve(arr, S)]))
    