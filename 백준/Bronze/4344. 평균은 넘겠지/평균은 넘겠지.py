C = int(input())


for _ in range(C):
    string = list(map(int, input().split()))
    
    a = []
    for i in range(0,string[0]):
        a.append(string[i+1])
    avg_a = sum(a)/len(a)

    b = 0
    for i in a:
        if i > avg_a:
            b += 1

    print(f'{b/(len(a))*100:.3f}%')
