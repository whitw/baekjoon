N = int(input())
s = []
for i in range(N):
    s.append(input())

for i in zip(*s):
    c = i[0]
    q = False
    for j in i:
        if j != c:
            q = True
            break
    print('?' if q else c, end='')