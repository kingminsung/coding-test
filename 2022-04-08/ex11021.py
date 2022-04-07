# 백준 11021
# A+B - 7
import sys

T = int(sys.stdin.readline())
result = [0] * T

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    result[i] = A+B

for i in range(T):
    print("Case #%d: %d" %(i+1, result[i]))

"""
for i in range(T):
    print("Case #", end='') # end='' 줄바꿈('\n')을 없앰
    print(i+1, "\b:", result[i])
"""