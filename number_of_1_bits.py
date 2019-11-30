import unittest

def hamming_weight(n):
    bit_string = ''
    while n:
        if n & 1 == 1:
            bit_string = '1' + bit_string
        else:
            bit_string = '0' + bit_string
        n //= 2
    count = 0
    for bit in bit_string:
        if bit == '1':
            count += 1
    return count

        