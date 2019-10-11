words = input()
words = words.upper()
alpha_set = set()

for w in words:
    alpha_set.add(w)
alpha = list(alpha_set)
cnt_lst = []

for a in alpha:
    cnt = words.count(a)
    cnt_lst.append((cnt, a))
cnt_lst.sort(reverse=True)

max_num = max(cnt_lst)[0]

length = 0
for c in cnt_lst:
    if c[0] == max_num:
        length += 1

if length == 1:
    print(max(cnt_lst)[1])
else:
    print('?')