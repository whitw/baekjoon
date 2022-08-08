import sys
from functools import cmp_to_key
def compare(a, b):
    if a[1] == b[1]:
        return a[0]-b[0]
    return a[1]-b[1]

def solve(meetings):
    meetings = sorted(meetings, key=cmp_to_key(compare))
    endtime = 0
    result = 0
    for begin, end in meetings:
        if begin >= endtime:
            result += 1
            endtime = end
    return result


if __name__ == '__main__':
    read = sys.stdin.readline
    n = int(read())
    meetings = []
    for i in range(n):
        a, b = map(int, read().split())
        meetings.append((a, b))
    print(solve(meetings))