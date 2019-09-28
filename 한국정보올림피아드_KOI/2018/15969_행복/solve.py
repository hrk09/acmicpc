import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    scores = list(map(int, input().split()))
    scores.sort()
    res = scores[-1] - scores[0]
    print(res)

# 백준 제출할 때에는
n = int(input())
scores = list(map(int, input().split()))
scores.sort()
res = scores[-1] - scores[0]
print(res)