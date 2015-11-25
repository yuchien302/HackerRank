#!/bin/python3

import sys
from collections import defaultdict

N,M = input().strip().split(' ')
N,M = [int(N),int(M)]
S = input().strip()
count = 0

memo = {"GG":1, "GL":2, "LG":2, "LL":1}
q = [S]
while q:
    next_q = []
#    print(q)
    for s in q:
        if s in memo:
            count += memo[s]
        else:
            if s[0] == 'L':
                next_q.append(s[1:])
            if s[-1] == 'G':
                next_q.append(s[:-1])
            
            idx = 0
            while s.find('GL', idx) != -1:
                idx = s.find('GL', idx)
                next_q.append(s[:idx] + 'G' + s[idx+2:])
                next_q.append(s[:idx] + 'L' + s[idx+2:])                
                idx += 1
    q = next_q
    
print(count%M)    

