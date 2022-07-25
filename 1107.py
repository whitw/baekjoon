import sys
from collections import deque
import time

def pressable(i, broken):
    bi = str(i)
    for b in bi:
        if broken[int(b)]:
            return False
    return True

def solve(N, broken):
    #   N: 이동하고자 하는 채널 번호
    # 100: 시작 채널 번호
    # broken: 길이 10 배열.
    #   키 i가 망가졌다면 broken[i]=True, else False
    result = abs(N - 100)
    # result: 지금까지 관측한 것중 최소비용.
    # abs(N-100): 채널 100에서 +또는 -만 눌러서 이동했을 때 최소비용
    for i in range(1000000):
        #단순한 버전. 채널 i를 누를 수 있고
        #이때의 비용이 현재까지 최소비용보다 적으면 갱신
        if pressable(i, broken):
            li = len(str(i))
            if abs(N-i) + li < result:
                result = abs(N-i) + li
            elif li + i - N > result and i > N:
                #i가 증가하면 반드시 비용도 증가하는 경우
                break
    return result

if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    M = int(read())
    brokens = []
    if M != 0:
        brokens = map(int,read().split())
    broken = [False for _ in range(10)]
    for i in brokens:
        broken[i] = True
    begin = time.time()    
    print(solve(N, broken))
    end = time.time()
    #print("runtime=", end - begin, "s")