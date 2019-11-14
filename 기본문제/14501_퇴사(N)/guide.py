import sys
sys.stdin = open('input.txt', 'r')

def solution(x):
    global res
    if x == N:
        for i in range(N):
            if S[i]:
                for j in range(i+1, i+T[i]):
                    if j >= N or S[j]:
                        return
        tmp_sum = 0
        for i in range(N):
            if S[i]:
                tmp_sum += P[i]
        ans = max(res, tmp_sum)
    else:
        S[x] = 1
        solution(x+1)
        S[x] = 0
        solution(x+1)

TC = int(input())
for t in range(TC):
    N = int(input())
    T = [0]*N
    P = [0]*N
    S = [0]*N

    for i in range(N):
        T[i], P[i] = map(int, input().split())
    res = 0
    solution(0)

    print(res)