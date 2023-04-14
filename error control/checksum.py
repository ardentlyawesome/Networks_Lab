# Assume that Swetha want to transmit a set of bytes over noisy channel and she decided to use checksum for detecting error at the receiving side. Help her to find out checksum for the given set of bytes

# Input Format

# First line represents the numbe of bytes-n for which checksum needs to be calculated. 2 to n+1 lines represents each byte one by one.

# Constraints

# byte values are 0s and 1s.

# Output Format

# 8 bit checksum

# Sample Input 0

# 4
# 11001100
# 10101010
# 11110000
# 11000011
# Sample Output 0

# 11010011

n = int(input())
csum = 0
for i in range(0, n, 1):
    x = input()
    l = len(x)
    buffer = "1" + "0"*l
    csum += int(x, 2)
    if csum >= (2**l):
        csum -= int(buffer, 2)
        csum += 1
ssum = bin(csum)
ssum = ssum[2::]
buffer = "0"*(len(x) - len(ssum))
ssum = buffer + ssum
ones = ""
for i in range(0, len(ssum), 1):
    if ssum[i] == "0":
        ones += "1"
    else:
        ones += "0"
print(ones)