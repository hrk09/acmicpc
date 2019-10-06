'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3 // 총 단지수
7  // 단지 별 세대수
8
9
'''
# dfs로 풀었음. cnt 처리 유의

def dfs(i, j):
    global cnt
    # 방문처리
    g[i][j] = '0'
    cnt += 1
    # 해당 점 기준으로 상하좌우 조사
    for _ in range(4):
        ii = i + dx[_]
        jj = j + dy[_]
        # 범위 체크
        if ii < 0 or ii >= n or jj < 0 or jj >= n:
            continue
        # 그 부분이 1이면 그 부분 기준으로  dfs 진행함
        if g[ii][jj] == '1':
            dfs(ii, jj)
    return cnt

n = int(input())
g = [list(input()) for i in range(n)]
# print(g)
cnt = 0
res = []
# 상하좌우조사
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 시작점 조사
for i in range(n):
    for j in range(n):
        if g[i][j] == '1':
            # cnt 초기화
            cnt = 0
            dfs(i, j)
            res.append(cnt)

# 세대 수 오름차순
res.sort()
print(len(res))
for i in res:
    print(i)