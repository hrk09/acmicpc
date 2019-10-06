# 최단경로, bfs
import sys
sys.stdin = open('input.txt', 'r')

def bfs(x, y):
    global cnt
    q = []
    visit = []
    q.append([x, y])
    while q:
        node = q.pop(0)
        if node == [n, m]:
            return cnt
        else:
            if node[0] not in visit:
                visit.append(node[0])
                for i in range(1, m+1):
                    # print(g[node[0]][i])
                    if g[node[0]][i] == '1' and node[0] not in visit and [node[0], i] not in q:
                        print([node[0], i])
    #                     q.append([node[0], i])
    #                     cnt += 1
    # return cnt


TC = int(input())
for t in range(1):
    n, m = map(int, input().split())
    g = [['0']*(m+1)] + [['0'] + list(input()) for i in range(n)]
    # print(g)
    cnt = 0
    bfs(1, 1)

