import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for t in range(1):
    n, m = map(int, input().split())  # 세로 10/ 가로 13
    board = [list(input()) for i in range(m)]
    check_color = ['B', 'W']

    # 시작점 잡기
    for i in range(n-7):
        for j in range(i, m-7):
            for z in range(7):
            # for color in range(2):
            #     cnt = 0
            #     if board[i][j] != check_color[color%2]:
            #         cnt += 1
            #     color += 1