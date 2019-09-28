import sys
sys.stdin = open('input.txt', 'r')
# N개 색이라는 말에 유의해야 함

def res(c):
    res = 0
    for i in range(len(c)):
        if i == 0:
            res += c[1]-c[0]
        elif i == len(c)-1:
            res += c[-1]-c[-2]
        else:
            if c[i]-c[i-1] > c[i+1]-c[i]:
                res += c[i+1]-c[i]
            else:
                res += c[i]-c[i-1]
    return res

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    dot = []
    color = set()
    fin = 0

    for i in range(n):
        p, c = map(int, input().split())
        dot.append((p, c))
        color.add(c)

    # color 별로 tmp에 점 값 넣고 def 함수 돌리고 res를 fin에 더해주는 작업
    for c in color:
        # 색 하나 작업 끝나면 초기화
        tmp = []
        for d in dot:
            if d[1] == c:
                tmp.append(d[0])
        tmp.sort()
        fin += res(tmp)
    print('#{} {}'.format(t, fin))
