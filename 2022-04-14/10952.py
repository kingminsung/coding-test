# 백준 10952
# A+B - 5
import sys
result = [0] * 100
i = 0

while True:
    A, B = map(int, sys.stdin.readline().split())
    if (A==0) and (B==0):
        break
    result[i] = A + B
    i += 1

for j in range(i):
    print(result[j])