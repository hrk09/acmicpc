'''
14
36

3
18
'''
n = int(input())
clap_num = ['3', '6', '9']
clap = 0

for i in range(1, n+1):
    for j in range(len(str(i))):
        if str(i)[j] in clap_num:
            clap += 1
print(clap)
