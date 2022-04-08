# 백준 11022
# A+B - 8
import sys
T = int(sys.stdin.readline())
result = [0] * T
A = [0] * T
B = [0] * T
for i in range(T):
    A[i], B[i] = map(int, sys.stdin.readline().split())
    result[i] = A[i]+B[i]

for j in range(T):
    print("Case #%d: %d + %d = %d" %(j+1, A[j], B[j], result[j]))