import sys
sys.stdin = open('input.txt', 'r')

# bfs
def bfs(i, j):
    global day, unrip
    while tomato:
        # 시작값에서 뽑은 t
        t = tomato.pop(0)
        # 방향 조사
        for _ in range(4):
            nx = t[0] + dx[_]
            ny = t[0] + dy[_]
            # 범위 넘어가는 건 스킵함
            if nx < 0 or nx >= col or ny < 0 or ny >= row:
                continue
            elif farm[nx][ny] != 0:
                continue
            # 이동 했을 때, 해당 값이 0이면, 그걸 1로 바꾸고 날짜 +1 하고 bfs 또 돌림
            farm[nx][ny] = 1
            tomato.append([nx, ny])
            day += 1
            unrip -= 1
    return days

TC = int(input())
for t in range(1, TC+1):
    row, col = map(int, input().split())
    farm = []
    tomato = []
    unrip = 0
    # 2차원 그래프 만들기
    for c in range(col):
        farm.append(list(map(int, input().split())))
        for r in range(row):
            if farm[c][r] == 1:
                tomato.append([c, r])
            elif farm[c][r] == 0:
                unrip += 1
    # print(tomato)

    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    days = []
    day = 0
    print(day)

