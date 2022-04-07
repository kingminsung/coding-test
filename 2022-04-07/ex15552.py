# 백준 15552
import sys
num = int(sys.stdin.readline())
result = [0] * num

for i in range(num):
    A, B = map(int, sys.stdin.readline().split())
    result[i] = A+B

for i in range(num):
    print(result[i])