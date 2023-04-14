# Given an IPv4 classful address in dotted decimal notation, Find out whether the address is valid and its class

# Input Format

# IP address

# Constraints

# IP address is mentioned in dotted decimmal notation

# Output Format

# whether the address is valid. if so, its class

# Sample Input 0

# 28.34.54.12
# Sample Output 0

# Valid
# A
# Sample Input 1

# 28..54.12
# Sample Output 1

# Invalid
def validate_ip_address(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        return "Invalid"
    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return "Invalid"
    if int(octets[0]) >= 0 and int(octets[0]) <= 127:
        return "Valid\nA"
    elif int(octets[0]) >= 128 and int(octets[0]) <= 191:
        return "Valid\nB"
    elif int(octets[0]) >= 192 and int(octets[0]) <= 223:
        return "Valid\nC"
    elif int(octets[0]) >= 224 and int(octets[0]) <= 239:
        return "Valid\D"
    elif int(octets[0]) >= 240 and int(octets[0]) <= 255:
        return "Valid\nClass E"
    else:
        return "Invalid"
ip_address = input().strip()
print(validate_ip_address(ip_address))