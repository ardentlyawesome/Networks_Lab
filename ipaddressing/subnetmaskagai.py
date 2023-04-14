# Assume that an organization is given a network addres of _______. Administrator wants to create atleast _ number of subnets with equal number of computers. Find out the subnet mask and number of devices in each subnet.

# Input Format

# First line represents network address of format w.x.y.z/a where a represents the net mask

# Constraints

# 0<=w, x, y,z <=255 and a is a positive number

# Output Format

# display the subnet mask in the first line and number of devices in the secondline A.B.C.D n

# Sample Input 0

# 192.168.200.0/24
# 6
# Sample Output 0

# 255.255.255.224
# 32

import math

add = input()
n = int(input())
L = add.split('.')
aux = L[3].split('/')
if len(aux) == 2:
    mbits = int(aux[1]) + math.ceil(math.log(n, 2))
    dbits = 32 - mbits
    L[3] = aux[0]
else:
    dbits = 32
    L[3] = aux[0]
flag = 1
for i in L:
    if int(i) >= 256 or int(i) < 0:
        flag = 0
if flag == 1:
    mask = '1'*mbits + '0'*dbits
    L = []
    for i in range(0, len(mask), 8):
         L.append(str(int(mask[i:i+8], 2)))
    print('.'.join(L))
    print(2**dbits)
