import sys
import random

def solve(MP):
    MP = sorted(MP)
    result = 0
    defile_level = 1
    for mp in MP:
        if mp > defile_level:
            result += (mp - defile_level)
            #print(f"\tmp={mp}, defile_level={defile_level}")
            defile_level += 1
        elif mp == defile_level:
            defile_level += 1
    return result

if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    MP = []
    for i in range(N):
        MP.append(int(read()))
    print(solve(MP))