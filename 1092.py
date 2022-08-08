import sys

def solve(crane, boxes):
    b = len(boxes)
    boxes = sorted(boxes)
    loaded = [False for _ in range(b)]
    remain = b

    c = len(crane)
    crane = sorted(crane)
    craneidx = [b - 1 for _ in range(c)]
    if boxes[-1] > crane[-1]:
        return -1
    for i in range(c):
        while craneidx[i] != -1 and boxes[craneidx[i]] > crane[i]:
            if craneidx[i] >= 0:
                craneidx[i] -= 1
            
        # crane[i-1] < boxes[craneidx[i]] <= crane[i],
        # if crane[i-1] != crane[i]
    #print(f"crane   :{crane}")
    #print(f"craneidx:{craneidx}")
    #print(f"boxes   :{boxes}")
    turn = 0
    while True:
        for i in range(c):
            #if craneidx[i] != -1:
                #assert (boxes[craneidx[i]] <= crane[i])
            while craneidx[i] != -1 and loaded[craneidx[i]] == True:
                if craneidx[i] >= 0:
                    craneidx[i] -= 1
                else:
                    break
            if craneidx[i] == -1:
                continue
            loaded[craneidx[i]] = True
            #print(f"crane {i}(limit={crane[i]}) at craneidx={craneidx[i]} loaded boxes[{craneidx[i]}] (weight={boxes[craneidx[i]]})")
            remain -= 1
            #print(f"remain: {remain}")
        turn += 1
        #print(f"turn: {turn}")
        if remain <= 0:
            return turn

if __name__ == '__main__':
    read = sys.stdin.readline
    read()
    crane = list(map(int, read().split()))
    read()
    boxes = list(map(int, read().split()))
    print(solve(crane, boxes))