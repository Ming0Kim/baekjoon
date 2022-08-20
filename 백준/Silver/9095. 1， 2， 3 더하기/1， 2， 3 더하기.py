dic = {1:1, 2:2, 3:4}

def plus(number):
  if number in dic:
    return dic[number]
  
  dic[number] = plus(number-1) + plus(number-2) + plus(number-3)
  return dic[number]

T = int(input())
for _ in range(T):
  n = int(input())
  print(plus(n))