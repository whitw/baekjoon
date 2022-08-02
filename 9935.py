import sys
from collections import deque

def solve(a, b):
    #print('a, b = ', a, b)
    startpoint_stack = deque()
    character_stack = deque()
    for i, s in enumerate(a):
        #print('i, s =', i, s)
        if len(startpoint_stack) == 0:
            startpoint_stack.append(0)
        if startpoint_stack[-1] != -1 and s == b[startpoint_stack[-1]]:
            startpoint_stack[-1] += 1
            character_stack.append(s)
        elif s == b[0]:
            startpoint_stack.append(1)
            character_stack.append(s)
        else:
            startpoint_stack.append(-1)
            character_stack.append(s)
        if startpoint_stack[-1] == len(b):
            for i in range(len(b)):
                character_stack.pop()
            startpoint_stack.pop()
        #print('startpoint_stack=', ' '.join([str(i) for i in startpoint_stack]))
        #print('character_stack=', ' '.join(character_stack))
    result = ''.join(i for i in character_stack)
    if result == '':
        result = 'FRULA'
    return result

if __name__ == '__main__':
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()
    print(solve(a,b))