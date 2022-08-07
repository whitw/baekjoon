input()
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)
print(sum([i*j for i, j in zip(a, b)]))