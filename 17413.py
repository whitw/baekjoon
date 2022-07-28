import sys

def solve(S):
    ss = S.replace('>', '<').split('<')
    ss = [ss[i] if i % 2 == 1 else ss[i].split() for i in range(len(ss))]
    for i in range(0, len(ss), 2):
        ss[i] = [ss[i][j][::-1] for j in range(len(ss[i]))]
    result = ''
    for i, s in enumerate(ss):
        if i % 2 == 1: #tag
            result += '<' + s + '>'
        else: #not a tag
            result += ' '.join(s)
    return result

if __name__ == '__main__':
    S = sys.stdin.readline().rstrip()
    print(solve(S))