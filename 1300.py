def solve(N, k):
    ltk = 0 #이 숫자보다 작은 숫자들의 갯수가 반드시 k보다 적다
    gtk = 10**10+1 #이 숫자보다 작은 숫자들의 갯수가 k보다 많거나 같다
    while(ltk + 1 != gtk):
        testk = (ltk + gtk) // 2
        lttk = 0 #testk보다 작은 숫자들의 갯수
        for i in range(1, min(N, testk)+1):
            lttk += min(N, ((testk-1) // i))
        if lttk < k:
            ltk = testk
        else:
            gtk = testk
        #print(f"\ttestk={testk}, lttk={lttk}, k={k}")
    return ltk
    

def answer(N, k):
    testarr = [0]
    for i in range(1, N+1):
        for j in range(1, N+1):
            testarr.append(i*j)
    testarr = sorted(testarr)
    #print(testarr)
    return testarr[k]

def test(tries, N=10000):
    import random
    n_success=0
    n_fail=0
    for t in range(tries):
        N = random.randint(1, N)
        k = random.randint(1, N * N)
        s = solve(N,k)
        a = answer(N,k)
        if s != a:
            print(f"N, k = {N},{k}")
            print(f"expected {a}, got {s}")
            n_fail += 1
            input()
        else:
            n_success += 1
        if t % 10 == 0:
            print(f"\t{t} tries")
 
if __name__ == '__main__':
    N = int(input())
    k = int(input())
    print(solve(N,k))
    #print("answer:", answer(N, k))
    #test(10000, N=1000)
            