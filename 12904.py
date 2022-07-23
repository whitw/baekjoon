def solve(A:str, B:str):
    while(len(A) < len(B)):
        if(B[-1] == 'A'):
            B = B[:-1]
        else:
            B = B[:-1][::-1]
    if(A == B):
        return 1
    return 0


print(solve(input(), input()))