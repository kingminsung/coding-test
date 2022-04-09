# 백준 2439
# 별 찍기 - 2
import sys
N = int(sys.stdin.readline())

for i in range(1, N):
    print(" " * (N-i), end='')
    for j in range(i):
        print("*" * i)
# 이건 모르겠다