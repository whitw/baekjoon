import sys

def solve(C, house):
    N = len(house)
    house = sorted(house)
    max_dist = 10000000000 #절대로 C개의 공유기를 설치할 수 없다.
    min_dist = 0 #반드시 C개의 공유기를 설치할 수 있다.
    '''
    너무 어려우니까 천천히 생각하기
    첫 집에 공유기 하나를 두고, 거리가 test_dist 이상이면서 가장 가까운
    곳에 새로 공유기를 설치한다.
    새로 설치한 집을 다시 기준점으로 설정.
    이를 반복했을 때의 C를 측정한다.
    만약 끝까지 진행했을 때, C개의 공유기를 설치하지 못했다면 실패.
    C개의 공유기를 설치했다면 성공.
    '''
    idx = 0
    while(min_dist + 1 != max_dist):
        idx = 0
        #debug_installed_houses = [0]
        test_dist = (max_dist + min_dist) // 2
        test_C = C - 1
        for newidx in range(N):
            if house[newidx] - house[idx] >= test_dist:
                test_C -= 1
                idx = newidx
                #debug_installed_houses.append(house[idx])
            if test_C <= 0:
                break
        if test_C <= 0: #거리가 충분해 C개의 공유기를 설치할 수 있음. 더 벌려볼 수 있다.
            min_dist = test_dist
        else: #거리를 너무 넓게 잡아 C개의 공유기를 설치할 수 없음.
            max_dist = test_dist
        #print(f"test:dist({test_dist}), C({test_C}), install({debug_installed_houses})")
    return min_dist

if __name__ == '__main__':
    read = sys.stdin.readline
    N, C = map(int, read().split())
    house = []
    for i in range(N):
        house.append(int(read()))
    print(solve(C, house))