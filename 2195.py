def solve(S: str, P: str):
    begin, end, result = 0, len(P), 0
    while(begin < end):
        #print(begin, end, S, P, P[begin:end])
        if (S.find(P[begin:end]) == -1):
            begin += 1
        else:
            result += 1
            P = P[:begin]
            end = len(P)
            begin = 0
            
    return result

print(solve(input(), input()))
