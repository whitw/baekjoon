import sys

cleaned = 2
empty = 0
wall = 1

class Robot:
    def __init__(self, N, M, r, c, d, board):
        self.N = N
        self.M = M
        self.r = r
        self.c = c
        self.d = d
        self.board = board

    def left(self):
        return (self.d + 3) % 4

    def turnLeft(self):
        self.d = self.left()

    def front(self):
        err = False
        r, c = self.r, self.c
        if self.d == 1: #east
            c += 1
        elif self.d == 2: #south
            r += 1
        elif self.d == 3: #west
            c -= 1
        elif self.d == 0: #north
            r -= 1
        if r < 0 or r >= N or c < 0 or c >= M:
            err = True #out of border
        return err, r, c

    def see_front(self):
        err, r, c = self.front()
        if err:
            return wall
        return self.board[r][c]

    def go(self):
        err, r, c = self.front()
        if err:
            return False
        else:
            self.r, self.c = r, c
            return True

    def clean(self):
        self.board[self.r][self.c] = cleaned
    
    def debug(self):
        for i, _ in enumerate(self.board):
            for j, _ in enumerate(self.board[i]):
                if(i == self.r and j == self.c):
                    if self.d == 0:
                        print('^', end=' ')
                    if self.d == 1:
                        print('>', end=' ')
                    if self.d == 2:
                        print('V', end=' ')
                    if self.d == 3:
                        print('<', end=' ')
                else:
                    print(board[i][j], end=' ')
            print('')
        print('\n')

def step_2(robot):
    turnCnt = 0
    while(True):
        #robot.debug()
        robot.turnLeft()
        if robot.see_front() == empty:
            robot.go()
            do_continue = True
            return do_continue
        else:
            turnCnt += 1
            if turnCnt == 4:
                robot.turnLeft()
                robot.turnLeft()
                if robot.see_front() != wall:
                    robot.go()
                    robot.turnLeft()
                    robot.turnLeft()
                    turnCnt = 0
                    continue
                else:
                    robot.turnLeft()
                    robot.turnLeft()
                    do_continue = False
                    return do_continue


def run(robot):
    result = 0
    while(True):
        #assert(board[robot.r][robot.c] == empty)
        robot.clean()
        result += 1
        do_continue = step_2(robot)
        if do_continue:
            continue
        else:
            break
    return result



def solve(N, M, r, c, d, board):
    robot = Robot(N,M,r,c,d,board)
    return run(robot)
    


if __name__ == '__main__':
    read = sys.stdin.readline
    N, M = map(int, read().split())
    r, c, d = map(int, read().split())
    board = [[i for i in map(int,read().split())] for _ in range(N)]
    print(solve(N,M,r,c,d,board))