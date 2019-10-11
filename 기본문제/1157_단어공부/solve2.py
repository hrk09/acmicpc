words = input()
# 대문자로 받는 작업
words = words.upper()

# alpha 중복 없이 set에 저장하기
alpha_set = set()
for w in words:
    alpha_set.add(w)

# idxing 작업을 위해 set을 리스트로 변경함
alpha_lst = list(alpha_set)

# 알파벳, cnt 숫자로 된 리스트 작업
cnt_lst = []
for a in alpha_lst:
    cnt_lst.append((words.count(a), a))
cnt_lst.sort()

max_num = cnt_lst[-1][0]
d = 0

for c in cnt_lst:
    if cnt_lst[0] == max_num:
        d += 1

if d == 1:
    print(cnt_lst[-1][1])
else:
    print('?')



