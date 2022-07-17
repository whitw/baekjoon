import sys

def solve(arr):
    idx = len(arr) - 1
    maxprice = arr[idx]
    result = 0
    while(idx >= 0):
        if(arr[idx] < maxprice):
            result += maxprice - arr[idx]
        elif(arr[idx] > maxprice):
            maxprice = arr[idx]
        idx -= 1
    return result

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        sys.stdin.readline()
        print(solve([int(i) for i in sys.stdin.readline().split()]))

