# Assume that you are going to implement a part of GO BACK N ARQ FLOW control algorithm. Here are the terms used in algorithm.

# Sf: First frame sent out in the pipeline for whick acknowledgement is not yet received
# Sn : Next frame to be sent
# m: length of the sequence number
# Sw : Window size (2^m)-1
# Sf and Sn changes on any one of the following 3 possible evnts in Go back N ARQ

# Timeout (E1)
# Frames from from Upper layer(E2)
# ACK from bottom layer (E3)
# Given m Sf Sn E1 E2 E3 as input You need to find out the value of Sf and Sn for every test case.

# Input Format

# n m Sf Sn E1 E2 E3 (one line for each test case) n represents number of test cases

# Constraints

# m Sf and Sn >0 E1 can be either 0 (if no timeout) or 1 if there is a timeout E2 is the number of packets arrived from upper layer E3 is either 0 or acknowledgement number At a time any one of these 3 events can happen

# Output Format

# Sf Sn

# Sample Input 0

# 4
# 3 1 4 0 3 0
# 4 1 9 0 0 6
# 2 1 3 1 0 0
# 5 1 11 0 50 0
# Sample Output 0

# 1 7
# 6 9
# 1 3
# 1 32



# WRONG ANSWER

n = int(input())

for i in range(n):
    m, Sf, Sn, E1, E2, E3 = map(int, input().split())
    if E1 == 1:  # Timeout event
        Sn = Sf
    else:
        if E2 > 0:  # Frames from upper layer event
            if Sn - Sf < (2**m)-1:
                Sn += 1
        if E3 > 0:  # ACK from bottom layer event
            if Sf <= E3 <= Sn:
                Sf = E3 + 1

    print(Sf, Sn)