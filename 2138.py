import sys

def solve_case(s):
    result = 0
    for i in range(len(s) - 2):
        if s[i] == 1:
            result += 1
            s[i] = 0
            s[i+1] = 1 - s[i+1]
            s[i+2] = 1 - s[i+2]
    if s[-2] == 1:
        result += 1
        s[-2] = 0
        s[-1] = 1 - s[-1]
    if s[-1] == 1:
        return -1
    else:
        return result

def solve(s1, s2):
    diff = [(0 if s1[i] == s2[i] else 1) for i in range(len(s1))]
    #print(diff)
    '''
    너무 복잡해지기 전에 생각 정리
    루프를 돌 건데, '이미 계산을 한 것의 값을 바꾸는 것'은
    계산이 너무 어렵기 때문에 문제를 살짝 비틀어서 
    iter번째, iter+1번째, iter+2번째를 뒤집는 방식을 사용한다.
    첫 index는 -1이 되어야 하지만, 마찬가지로 -1 idx는 어색하기 때문에
    맨 앞에 숫자 하나를 추가하는 방식으로 문제를 비튼다.
    다만, 이 때 추가하는 숫자는 0과 1 모두에 대해 테스트해봐야 한다(?)
    어쩌면 더 좋은 방식이 있을 수 있지만, 도저히 규칙을 찾을 수 없었음.
    '''
    r1 = solve_case([1] + diff)
    r2 = solve_case([0] + diff)
    if r1 == -1:
        return r2
    if r2 == -1:
        return r1
    return min(r1, r2)


if __name__ == '__main__':
    _ = sys.stdin.readline()
    print(solve(sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()))

