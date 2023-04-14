# Assume that you are given data and Generator polynomial. Find out the data to be transmitted to the receiver using CRC.

# Input Format

# First line represents the Data- Dividend (n bits) Second line represents the Generator polynomial- Divisor (m bits)

# Constraints

# Both inputs consist of 0s and 1s m and n are positive integers m

# Output Format

# Single line which represents the data to be transmitted to the receiver Dividend(n bits)+Remainder(m-1 bits)

# Sample Input 0

# 10111011
# 1001
# Sample Output 0

# 10111011110

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0 : pick]
 
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1
        
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword

def encodeData(data, key):
 
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword 

        
data = input()
key = input()
print(encodeData(data,key))