# 백준 10951
# A+B - 4

import sys

"""for i in range(a):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
"""

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
    except:
        break
    print(A+B)