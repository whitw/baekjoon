import sys

def solve(N, lan):
    max_len = 2 ** 31 #N을 갖기 위해 이것보다는 짧아야 된다.
    min_len = 0# N을 갖기 위해 이 길이를 써도 된다.
    while(max_len != min_len + 1):
        test_len = (max_len + min_len) // 2 #랜선을 잘라 볼 길이단위
        test_N = 0
        #각 랜선을 test_len 단위로 잘랐을 때 얻을 수 있는 랜선의 갯수
        for l in lan:
            test_N += (l // test_len)
        if test_N >= N: #너무 과다하게 만들었다. 이것보다는 길게 만들어도 됨.
            min_len = test_len
        else: #부족하다. 무조건 이것보다 짧아야 함. 
            max_len = test_len
        #print(f"min_len:{min_len}, max_len:{max_len}, test_len:{test_len}, test_N:{test_N}")
    return min_len


if __name__ == '__main__':
    read = sys.stdin.readline
    K, N = map(int, read().split())
    lan = []
    for i in range(K):
        lan.append(int(read()))
    print(solve(N, lan))