def solution(numbers):
    answer = -10**8
    length = len(numbers)
    for i in range(0, length-1):
        for j in range(i+1, length):
            if numbers[i]*numbers[j] > answer:
                answer = numbers[i]*numbers[j]
    return answer