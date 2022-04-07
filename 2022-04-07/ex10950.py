# 백준 10950
num = int(input())
add = [0] * num
for i in range(num):
    a, b = map(int, input().split())
    add[i] = a + b

for i in range(num):
    print(add[i])