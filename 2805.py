from re import L
import sys

def solve(M, tree):
    max_height = 1000000001 #이 높이에서 자르면 절대 M 이상의 나무를 얻을 수 없다.
    min_height = 0 #이 높이에서 자르면 반드시 M 이상의 나무를 얻을 수 있다.
    #최적해는 min_height+1=max_height일 때 min_height
    while(min_height+1 != max_height):
        test_height = (min_height + max_height) // 2
        test_M = 0
        for t in tree:
            wood = t - test_height
            wood = wood if wood > 0 else 0
            test_M += wood
            #print(f"\ttest_M += {wood} , test_M = {test_M}, t={t}, test_height={test_height}")
        
        if test_M >= M: #원하는 만큼 나무를 얻었음.
            min_height = test_height
        else: #원하는 만큼 나무를 얻지 못했음.
            max_height = test_height
        #print(f"{min_height}/{test_height}/{max_height}, test_M={test_M}")
    return min_height

if __name__ == '__main__':
    read = sys.stdin.readline
    _, M = map(int, read().split())
    tree = list(map(int, read().split()))
    print(solve(M, tree))