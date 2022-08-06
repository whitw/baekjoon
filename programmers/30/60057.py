def solution(s):
    n = len(s)
    shortest_len = n
    for l in range(1, n):
        last_part = ''
        idx = 0
        result = ''
        cnt = 1
        while(idx + l <= n):
            part = s[idx:idx+l]
            if last_part == part:
                cnt += 1
            else:
                if cnt != 1:
                    result += str(cnt)
                result += last_part

                cnt = 1
                last_part = part
            idx += l
        if cnt != 1:
            result += str(cnt)
        result += last_part
        result += s[idx:]
        #print(f"{l}:{result}")
        if len(result) < shortest_len:
            shortest_len = len(result)
        
    return shortest_len
    #속도 효율 ㅈ도 안챙겼는데 이게 되네

if __name__ == '__main__':
    print(solution(input().rstrip()))