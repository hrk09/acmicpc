'''
3
happy
new
year
4
aba
abab
abcabc
a

3
4
'''
num = int(input())
words = [input() for n in range(num)]
w_set = set()
cnt = 0
for word in words:
    for w in word:
        w_set.add(w)
    for i in range(len(word)):
        while word[i] != words[i+1]:
            idx = i
            break
        print(idx)
        # if w in words[idx:]:




