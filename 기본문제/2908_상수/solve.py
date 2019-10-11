'''
734 893

437
'''
a, b = input().split()

a = list(a); b = list(b)
a.reverse(); b.reverse()
sa = ''
sb = ''
for i in range(3):
    sa += a[i]; sb += b[i]
# print(sa, sb)

if int(sa) < int(sb):
    print(sb)
else:
    print(sa)
