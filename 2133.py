def solve(N):
    DP = [[0 for _ in range(7)] for _ in range(N+1)] #비트마스크 사용
    DP[0][0] = DP[0][3] = DP[0][6] = 1
    for i in range(1, N+1):
        DP[i][0] = DP[i-2][3] + DP[i-2][6] + DP[i-2][0]
        DP[i][1] = DP[i-1][6]
        DP[i][2] = DP[i-1][5]
        DP[i][3] = DP[i][0] + DP[i-1][4]
        DP[i][4] = DP[i-1][3]
        DP[i][5] = DP[i-1][2]
        DP[i][6] = DP[i-1][1] + DP[i][0]
    #for i in range(N+1):
    #    print(DP[i])
    return DP[N][0]
    


if __name__ == '__main__':
    print(solve(int(input())))