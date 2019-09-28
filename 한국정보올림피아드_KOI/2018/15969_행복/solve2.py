import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1, TC+1):
    n = int(input())
    scores = list(map(int, input().split()))
    print(max(scores) - min(scores))