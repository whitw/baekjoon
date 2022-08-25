import sys
from collections import Counter

read = sys.stdin.readline
N = int(read())
numbers = []
counter = Counter()
for i in range(N):
    numbers.append(int(read()))
    
numbers = sorted(numbers)
counter = Counter(numbers)
print('--------------------')
print(round(sum(numbers)/N))
print(numbers[(N-1)//2])
cnt = sorted(counter.most_common(), key=lambda x:-x[1])
if N == 1:
    print(cnt[0][0])
elif cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(numbers[-1] - numbers[0])