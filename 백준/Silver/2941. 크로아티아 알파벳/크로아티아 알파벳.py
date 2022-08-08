cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = input()
cnt = 0
for i in cro:
    if i in N:
        cnt += N.count(i)
        N = N.replace(i,' ')
N = N.replace(' ','')
print(cnt+len(N))