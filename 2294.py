import sys
INF = 10001

def solve(k, coins):
    #DP[i]; i원을 만들기 위해 필요한 동전의 최소갯수
    DP = [INF for _ in range(k+1)]
    DP[0] = 0
    for i in range(k+1):
        for c in coins:
            if i - c >= 0 and DP[i-c]+1 < DP[i]:
                DP[i] = DP[i-c]+1
    if DP[k] == INF:
        return -1
    return DP[k]

if __name__ == '__main__':
    read = sys.stdin.readline
    n, k = map(int, read().split())
    coins = []
    for i in range(n):
        coin = int(read())
        if coin <= k:
            coins.append(coin)
    print(solve(k, coins))