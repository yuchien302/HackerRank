#!/bin/python3

import sys
from fractions import gcd

A,B,C,D = input().strip().split(' ')
A,B,C,D = [int(A),int(B),int(C),int(D)]
print(sum([1 for a in range(1, A+1)
             for b in range(1, B+1)
             if abs(a-b) % 3 == 0
             for c in range(1, C+1)
             if (b+c) % 5 == 0 and (a*c) % 4 == 0
             for d in range(1, D+1)
             if gcd(a, d) == 1]))
