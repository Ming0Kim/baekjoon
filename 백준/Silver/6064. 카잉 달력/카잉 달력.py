# 시간초과
# # 최대공약수
# def GCD(x, y):
#     while y:
#         x, y = y, x%y
#     return x
# # 최소공배수
# def LCM(x, y):
#     result = (x*y) // GCD(x, y)
#     return result
#
# # 초기화
# t = int(input())
# for _ in range(t):
#     m, n, x, y = map(int, input().split())
#     result = -1
#     cnt = 0
#     while cnt <= LCM(m, n):
#         cnt += 1
#         a = cnt%m
#         b = cnt%n
#         if (a, b) == (x, y):
#             result = cnt
#             break
#     print(result)

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    val = -1
    while x <= m*n:
        if x % n == y%n:
            val = x
            break
        x += m
    print(val)