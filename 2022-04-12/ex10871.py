# 백준 10871
# X보다 작은 수
import sys

N, X = map(int, sys.stdin.readline().split())

A = [0] * N

A = list(map(int, sys.stdin.readline().split()))

for i in range(len(A)):
    if A[i] < X:
        print("%d " % A[i], end='')