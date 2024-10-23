
def calculate_redundant_bits(m):
    # Calculate the number of redundant bits (r) needed
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def hamming_encode(data):
    m = len(data)  # Number of data bits
    r = calculate_redundant_bits(m)
    n = m + r  # Total length (data + redundant bits)
    
    # Create an array to store the encoded data
    code = ['0'] * (n + 1)

    # Place data bits in their correct positions
    j = 0
    for i in range(1, n + 1):
        if i == 2**j:  # Parity bit positions (1, 2, 4, 8...)
            j += 1
        else:
            code[i] = data[-(i - j)]  # Reverse to match positions

    # Calculate the parity bits
    for i in range(r):
        parity_position = 2 ** i
        parity_value = 0
        for j in range(1, n + 1):
            if j & parity_position:
                parity_value ^= int(code[j])
        code[parity_position] = str(parity_value)

    return ''.join(code[1:])

def hamming_decode(code):
    n = len(code)  # Total length of the codeword
    r = calculate_redundant_bits(n)  # r = redundant bits count

    # Detect if there's an error by checking the parity bits
    error_pos = 0
    for i in range(r):
        parity_position = 2 ** i
        parity_value = 0
        for j in range(1, n + 1):
            if j & parity_position:
                parity_value ^= int(code[j - 1])
        if parity_value != 0:
            error_pos += parity_position

    # Correct the error if found
    if error_pos:
        print(f"Error at position: {error_pos}")
        code = list(code)
        code[error_pos - 1] = '1' if code[error_pos - 1] == '0' else '0'

    # Extract the original data
    data = []
    for i in range(1, n + 1):
        if i != 2 ** (i.bit_length() - 1):
            data.append(code[i - 1])

    return ''.join(data)

# Example usage
sender = input("sender input : ")
encoded = hamming_encode(sender)
print(f"Encoded data : {encoded}")

# Simulate error in the encoded message
reciver  = input("reciver input : ")
decoded = hamming_decode(reciver)
print(f"Decoded: {decoded[::-1]}")








