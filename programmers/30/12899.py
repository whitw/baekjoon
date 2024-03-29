def solution_old(n):
    ternary = []
    answer = ''
    while(True):
        ternary = [n % 3] + ternary
        n = n // 3
        if n == 0:
            break
    #print(ternary)
    for i in range(len(ternary)-1, 0, -1):
        if ternary[i] <= 0:
            ternary[i-1] -= 1
            ternary[i] += 3
            #print(f"update:{ternary}")
    #print(ternary)
    for i in ternary:
        if i != 0:
            if i == 3:
                answer += '4'
            else:
                answer += str(i)
    return answer

def solution(n):
    answer = ''
    arr = ['1', '2', '4']
    while n != 0:
        q, r = divmod(n-1, 3)
        answer = arr[r] + answer
        n = q
    return answer

if __name__ == '__main__':
    print(solution(int(input())))