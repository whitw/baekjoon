import sys
from collections import deque
import time

def pressable(broken):
    buttons = sorted([i for i in range(len(broken)) if not broken[i]])
    pressed = deque(buttons)
    while(True): #while not empty
        if not pressed:
            return 
        item = pressed.popleft()
        yield item
        for b in buttons:
            if item * 10 + b != item:
                pressed.append(item * 10 + b)

def solve(N, broken):
    #   N: 이동하고자 하는 채널 번호
    # 100: 시작 채널 번호
    # broken: 길이 10 배열.
    #   키 i가 망가졌다면 broken[i]=True, else False
    result = abs(N - 100)
    # result: 지금까지 관측한 것중 최소비용.
    # abs(N-100): 채널 100에서 +또는 -만 눌러서 이동했을 떄 최소비용
    for i in pressable(broken):
        # 누를 수 있는 채널들을 지속적으로 가져온다.
        if abs(N - i) + len(str(i)) < result:
            result = abs(N - i) + len(str(i))
        elif i > N and len(str(i)) + i - N > result:
            #i는 계속해서 커지는 형태. 채널 i에서 -로 이동했을 때 비용이
            #이미 최소보다 크다면 채널이 더 커져봤자 이득이 없음.
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