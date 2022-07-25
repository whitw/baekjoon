import sys
from collections import deque
import time

def pressable(broken, max_val):
    buttons = sorted([i for i in range(len(broken)) if not broken[i]])
    pressed = deque(buttons)
    while(True): #while not empty
        if not pressed:
            return 
        item = pressed.popleft()
        if item > max_val:
            return
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

    for i in pressable(broken, max_val=1000000):
        if abs(N - i) + len(str(i)) < result:
            result = abs(N - i) + len(str(i))
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
    print(end - begin)