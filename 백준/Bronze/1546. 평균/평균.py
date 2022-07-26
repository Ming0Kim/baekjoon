N = int(input())
subject = list(map(int, input().split()))
print(sum(subject)/max(subject)*100/N)
