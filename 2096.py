import sys

if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    arr = list(map(int, read().split()))
    MDP, mDP, nMDP, nmDP = [[i for i in arr] for _ in range(4)]
    print(f"read: {arr}")
    print(f"DP: {MDP}, {mDP}")
    
    for i in range(1, N):
        arr = list(map(int, read().split()))
        nMDP[0] = max(MDP[:2]) + arr[0]
        nmDP[0] = min(mDP[:2]) + arr[0]
        nMDP[1] = max(MDP) + arr[1]
        nmDP[1] = min(mDP) + arr[1]
        nMDP[2] = max(MDP[1:]) + arr[2]
        nmDP[2] = min(mDP[1:]) + arr[2]
        MDP, nMDP = nMDP, MDP
        mDP, nmDP = nmDP, mDP
        print(f"read: {arr}")
        print(f"DP: {MDP}, {mDP}")
    print(f"{max(MDP)} {min(mDP)}")