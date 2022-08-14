N = int(input())
cnt = [0] * 26
for i in range(N):
    cnt[ord(input()[0]) - ord('a')] += 1
printed=False
for i in range(26):
    if cnt[i] >= 5:
        print(chr(ord('a') + i), end='')
        printed = True
if not printed:
    print("PREDAJA", end='')