result = 0
for i in range(8):
    s = input()
    for j in range(8):
        result += (1 if s[j]=='F' else 0) * ((i+j+1) % 2)
print(result)