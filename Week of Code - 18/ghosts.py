#!/bin/python3

import sys


K,N = input().strip().split(' ')
K,N = [int(K),int(N)]
R = [int(R_temp) for R_temp in input().strip().split(' ')]
x = []
count = 0
for x_i in range(N):
    (x, y) = [int(x_temp) for x_temp in input().strip().split(' ')]
    target = (x*x + y*y)**0.5
#    print((x*x + y*y)**0.5)
#    print(R)

    left, right = 0, len(R)
    while left < right and left < len(R):
        mid = (left+right) // 2
        if R[mid] >= target:
            left = mid + 1
        else:
            right = mid
    count += left
#    print(left)
print(count)    
        
