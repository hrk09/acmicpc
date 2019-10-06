# 브루트포스
'''
5
55 185
58 183
88 186
60 175
46 155

2 2 1 2 5
'''
n = int(input())
rank = [0]*n
vol_info = [tuple(map(int, input().split())) for i in range(n)]
ans = []
for i in range(len(vol_info)):
    cnt = 1
    for j in range(len(vol_info)):
        if vol_info[i][0] < vol_info[j][0] and vol_info[i][1] < vol_info[j][1]:
            cnt += 1
    ans.append(cnt)
print(' '.join([str(a) for a in ans]))
