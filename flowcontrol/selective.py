# Assume that you need to implement SELECTIVE REPEATARQ FLOW control algorithm. Here are the terms used in algorithm.

# Sf: First frame sent out in the pipeline for whick acknowledgement is not yet received
# Sn: Next frame to be sent
# m: length of the sequence number
# Sw: Window size (2^m-1)
# Sf and Sn changes on any one of the following 3 possible evnts in Go back N ARQ 1. Timeout (E1) 2. Frames from from Upper layer(E2) 3. ACK OR NAK from bottom layer (E3) Given m Sf Sn E1 E2 E3 as input You need to find out the value of Sf and Sn for every test case.

# Input Format

# n m Sf Sn E1 E2 E3 (one line for each test case) n represents number of test cases

# Constraints

# m Sf and Sn >0 E1 can be either 0 (if no timeout) or 1 if there is a timeout E2 is the number of packets arrived from upper layer E3 is either 0 or acknowledgement number or negative acknowledgement number At a time any one of these 3 events can happen

# Output Format

# Sf Sn

# Sample Input 0

# 4
# 4 1 4 0 3 0
# 5 1 9 0 0 6
# 3 2 3 2 0 0
# 5 1 11 0 0 -5
# Sample Output 0

# 1 7
# 6 9
# 2 3
# 5 11

#WRONG CODE
# get number of test cases
n = int(input())

# process each test case
for i in range(n):
    # read input values for current test case
    m, sf, sn, e1, e2, e3 = map(int, input().split())

    # initialize Sf and Sn based on input values
    if e1 == 1:
        Sf = sf
        Sn = sf
    else:
        Sf = sf
        Sn = sn

    # check which event has occurred
    if e2 > 0:
        # frames from upper layer
        num_frames = min(e2, Sn - Sf + 1)
        Sn += num_frames
    elif e3 != 0:
        # ACK or NAK from bottom layer
        if Sf <= e3 < Sn:
            Sf = e3 + 1

    # output Sf and Sn for current test case
    print(Sf, Sn)