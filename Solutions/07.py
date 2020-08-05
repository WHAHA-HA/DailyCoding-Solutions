'''
Problem:

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of
ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka',
and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def count_decoding(digits: str) -> int:
    len_digits = len(digits)
    # dynamic Programming table
    count = [0] * (len_digits + 1)
    count[0] = 1
    count[1] = 1

    for i in range(2, len_digits + 1):
        count[i] = 0
        # if the last digit is not 0, then last digit must add to the number of words
        if digits[i - 1] > '0':
            count[i] = count[i - 1]
        # if second last digit is smaller than 2 and last digit is smaller than 7, then
        # last two digits form a valid character 
        if digits[i - 2] == '1' or (digits[i - 2] == '2' and digits[i - 1] < '7'): 
            count[i] += count[i - 2]
    return count[len_digits]


# DRIVER CODE
print(count_decoding('81'))
print(count_decoding('11'))
print(count_decoding('111'))
print(count_decoding('1311'))
print(count_decoding('1111'))
