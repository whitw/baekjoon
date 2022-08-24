import sys
import time

def timeit(f):
    def wrapper(*args, **kwargs):
        begin = time.time()
        val = f(*args, **kwargs)
        end = time.time()
        print(f"time: {end - begin}s")
        return val
    return wrapper
'''
@timeit
def solve(k, coins):
    coins = sorted(coins)
    DP = [0 for _ in range(k+1)]
    DPNew = [0 for _ in range(k+1)]
    DP[0] = 1
    for c in coins:
        for i in range(k+1):
            DPNew[i] = 0
            for j in range(i, -1, -c):
                #print(f"\tc, i, j = {c}, {i}, {j}")
                DPNew[i] += DP[j]
                #print(f"\t\tDPNew[{i}] += DP[{j}]")
        #print(f"DP\n{DP}\nDPNew\n{DPNew}")
        DP, DPNew = DPNew, DP
    return DP[k]
'''

def solve(k, coins):
    DP = [0 for _ in range(k+1)]
    for c in coins:
        DP[c] += 1
        for i in range(c+1, k+1):
            DP[i] += DP[i - c]
    return DP[k]

if __name__ == '__main__':
    read = sys.stdin.readline
    n, k = map(int,read().split())
    coins = []
    for _ in range(n):
        coin = int(read())
        if coin <= k:
            coins.append(coin)
    print(solve(k, coins))
