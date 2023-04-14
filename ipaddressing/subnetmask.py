# An organization is granted the block ________. The administrator wants to have ____ number of devices in each subnet. fIND OUT THE subnet mask.

# Input Format

# 130.56.128.0/17 128

# Constraints

# Input IP in dotted decimal notation

# Output Format

# 255.255.255.128

import math

add = input()
n = int(input())
dbits = math.ceil(math.log(n, 2))
mbits = 32 - dbits
mask = '1'*mbits + '0'*dbits
L = []
for i in range(0, len(mask), 8):
    L.append(str(int(mask[i:i+8], 2)))
print('.'.join(L))