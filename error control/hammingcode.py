# For the given set of code words (Consisting of 0s and 1s) , find out the minimum hamming distance.

# Input Format

# First line represents the number of codeword n From second line to (n+1)th line, each represents a codeword

# Constraints

# length of code word is >0 and <=8 No two words will be same.

# Output Format

# single integer representing minimum hamming distance

# Sample Input 0

# 4
# 0000
# 1010
# 1111
# 0110
# Sample Output 0

# 2

n = int(input())
l = []
for i in range(0, n):
    x = input()
    l.append(x)

distl = []
distval = []
for i in range(0, n):
    for j in range(i+1, n):
        xorcheck = ""
        dist = 0
        for k in range(0, len(l[0])):
            if(l[i][k] != l[j][k]):
                xorcheck += "1"
                dist += 1
            else:
                xorcheck += "0"
        distl.append(xorcheck)
        distval.append(dist)
print(min(distval))