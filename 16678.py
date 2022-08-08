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
#    MP = [random.randint(1, 20) for _ in range(random.randint(1, 20))]
#    print(MP)
#    print(sorted(MP))
#    assert(solve([1,3,5,5,6,8,9,11,12,13,13,14,14,15,15,16,18,19]) == 26)
#    assert(solve([7,3,6,2,4])==7)
#    assert(solve([1,2,3,4,5,6,7,8,9,10]) == 0)
#    assert(solve([0,1,1,1,1,1,1,1,1,1,1]) == 0)
#    assert(solve([1,2,2,2,2,2,2,2,2,2,2,2]) == 0)
#    assert(solve([1,2,3,4,5,6,8,8,9,10]) == 1)
