import sys

def dragon_curve(d, g):
    result = [d]
    for _ in range(g):
        #지금까지 작성된 내용을 끝점을 중심으로 시계방향으로 돌려야 한다.
        #시작점을 기준으로 90도 회전시켜 읽으면 새로운 부분과 동일한 모양이 되지만,
        #순서는 반대가 된다. 따라서 순서를 반전시키고, 방향을 반전시킨다.
        #방향을 반전시킬 경우 (i+3) % 4로 연산한 것에 (i+2) % 4를 하면 그 방향을 구할 수 있다.
        #따라서 최종적으로 방향은 (i+1) % 4와 같다.
        result += [(i + 1) % 4 for i in result][::-1]
    return result

def dir_to_2d_dir(dir):
    return [(0,1),(-1,0),(0,-1),(1,0)][dir]

def solve(curves):
    map = [[0 for _ in range(101)] for _ in range(101)]
    for curve in curves:
        y,x,d,g = curve
        directions = dragon_curve(d,g)
        map[x][y] = 1
        for dir in directions:
            dx,dy =dir_to_2d_dir(dir) 
            x += dx
            y += dy
            map[x][y] = 1
    result = 0
    for i in range(100):
        for j in range(100):
            if 1 == map[i][j] == map[i+1][j] == map[i][j+1] == map[i+1][j+1]:
                result += 1
    return result

if __name__ == '__main__':
    read = sys.stdin.readline
    N = int(read())
    curves = []
    for i in range(N):
        curve = map(int,read().split())
        curves.append(curve)
    print(solve(curves))
