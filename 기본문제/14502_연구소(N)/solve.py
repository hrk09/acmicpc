import sys
sys.stdin = open('input.txt', 'r')


TC = int(input())
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for i in range(N)]
