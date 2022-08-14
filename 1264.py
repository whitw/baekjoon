while True:
    result = 0
    line = input().rstrip().lower()
    if line == '#':
        break
    for i in line:
        if i in 'aeiou':
            result += 1
    print(result)