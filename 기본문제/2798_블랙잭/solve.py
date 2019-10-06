# 브루트 포스
'''
5 21
5 6 7 8 9
'''
n, m = map(int, input().split())
# n 장 중 3장 뽑아서 m에 최대한 근접한 3장 합 계산하기
cards = list(map(int, input().split()))
res = []
# 조합문제
for i in range(n-2):
    for j in range(i+1, n-1):
        for z in range(j+1, n):
            s = cards[i]+cards[j]+cards[z]
            if s <= m:
                res.append(s)
res.sort()
print(res[-1])