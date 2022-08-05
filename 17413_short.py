s=input().replace('>','<').split('<')
print(''.join([f'<{s[i]}>'if i%2 else' '.join([j[::-1]for j in s[i].split()])for i in range(len(s))]))