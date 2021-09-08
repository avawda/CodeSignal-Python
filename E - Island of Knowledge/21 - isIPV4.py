# Codewriting

# 300

# An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

# Given a string, find out if it satisfies the IPv4 address naming rules.

# Example

# For inputString = "172.16.254.1", the output should be
# isIPv4Address(inputString) = true;

# For inputString = "172.316.254.1", the output should be
# isIPv4Address(inputString) = false.

# 316 is not in range [0, 255].

# For inputString = ".254.255.0", the output should be
# isIPv4Address(inputString) = false.

# There is no first number.

def isIPv4Address_OPTIMAL(s):
    p = s.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

def isIPv4Address(inputString: str):
    output = True
    # Count Dots 
    dotCount = inputString.count(".")
    if dotCount != 3:
        return False
    
    for addr in inputString.split("."):
        if (len(addr) == 0) or (not addr.isnumeric() or int(addr) > 255):
            output = False
            break
        
        # Exclude fake text numbers between 00 and 09
        if (str(int(addr)) != addr):
            output = False
            break

    return output

testData = "64.233.161.00"
print(isIPv4Address(testData))


