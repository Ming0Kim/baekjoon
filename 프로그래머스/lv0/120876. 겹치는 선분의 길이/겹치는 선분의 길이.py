def solution(lines):
    answer = 0
    zone = [0]*201
    for line in lines:
        a, b = line[0], line[1]
        for i in range(a, b):
            zone[i] += 1

    for i in zone:
        if i>1:
            answer += 1
    return answer