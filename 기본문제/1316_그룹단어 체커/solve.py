n = int(input())
ans = 0
for i in range(n):
    word = list(input())
    # 인덱스 접근
    for k in range(len(word)):
        # word의 k번째 인덱스가 마지막 인덱스가 아니고, k번째와 k+1번째 알파벳이 같으면, 넘어감
        if k != len(word)-1 and word[k] == word[k+1]:
            continue
        # 그러나, k+1번째 이후에서 word[k] 알파벳이 나타난다면, break
        elif word[k+1:].count(word[k]):
            break
        # k인덱스가 마지막 인덱스가 되면, 그룹단어이므로 answer에 1더함
        elif k == len(word)-1:
            ans += 1
print(ans)




