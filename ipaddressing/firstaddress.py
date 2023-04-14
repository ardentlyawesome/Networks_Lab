# Assume that you are given an IP address of a device present in an organization along with the net mask.Find out the network address, last address and the total number of devices in the network.

# Input Format

# A single IP address on the format w.x.y.z/a

# Constraints

# w,x,y,z are numbers between 0 and 255 (Both inclusive) a is a positive number

# Output Format

# Network address last address number of devices

# Sample Input 0

# 192.68.5.5/24
# Sample Output 0

# 192.68.5.0
# 192.68.5.255
# 256

add = input()
L = add.split('.')
aux = L[3].split('/')
if len(aux) == 2:
    mbits = int(aux[1])
    dbits = 32-mbits
    L[3] = aux[0]
else:
    dbits = 32
    L[3] = aux[0]
flag = 1
for i in L:
    if int(i) >= 256 or int(i) < 0:
        flag = 0
if flag == 1:
    b = []
    for i in L:
        x = bin(int(i))[2::]
        l = len(x)
        s = '0'*(8 - l) + x
        b.append(s)
    bits = ''.join(b)
    b1 = bits[0:mbits] + '0'*dbits
    b2 = bits[0:mbits] + '1'*dbits
    L1 = []
    L2 = []
    for i in range(0, len(bits), 8):
        L1.append(str(int(b1[i:i+8], 2)))
        L2.append(str(int(b2[i:i+8], 2)))
    print('.'.join(L1))
    print('.'.join(L2))
    print(2**dbits)
