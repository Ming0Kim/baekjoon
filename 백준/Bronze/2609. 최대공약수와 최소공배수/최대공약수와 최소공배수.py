N, M = map(int, input().split())
a, b = min(N, M), max(N, M)
c, d = a, b
# 시간초과난 소중한 내 코드

# # 최대공약수 N, M 중에 작은 수부터 거꾸로 나눠서 0이 나오면,
# for i in range(a, 0, -1):
#     if N%i == 0 and M%i == 0:
#         print(i)
#         break
# # 최소공배수 N, M 중에 큰 수 부터 나눠서 0이 나오면,
# while True:
#     if b%N == 0 and b%M ==0:
#         print(b)
#         break
#     else:
#         b += 1

# 유클리드 호제법
while b!= 0:
    a = a%b
    a, b = b, a
print(a)
print(c*d//a)  # // 대신 / 쓰면 float형 나옴