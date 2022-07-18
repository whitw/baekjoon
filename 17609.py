import sys

def is_palindrome(s):
    return s == s[::-1]

def solve(s):
    idx_l = 0
    idx_r = len(s) - 1
    while(idx_l < idx_r):
        if s[idx_l] == s[idx_r]:
            idx_l += 1
            idx_r -= 1
        else:
            if is_palindrome(s[:idx_l] + s[idx_l + 1:]) or is_palindrome(s[:idx_r] + s[idx_r + 1:]):
                return 1
            else:
                return 2
    return 0

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        print(solve(sys.stdin.readline().rstrip()))