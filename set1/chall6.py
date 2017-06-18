#!/usr/bin/python

import os, sys, base64, binascii
from chall3 import decode_single_xor
import random

INT_MIN = 0xfffff

def binary_stream(string):
    return ''.join(map(lambda x: '{0:08b}'.format(ord(x)), string))

def find_hamming_distance(string1, string2):
    _string1 = binary_stream(string1)
    _string2 = binary_stream(string2)
	
    h_distance = 0
	
    for ch1, ch2 in zip(_string1, _string2):
        if (ch1 == '1' and ch2 == '0') or (ch1 == '0' and ch2 == '1'):
            h_distance += 1
    return float(h_distance)

# print find_hamming_distance('wokka wokka!!!', 'this is a test')

# sys.exit()

def find_key_size(string):
    sum_h_distance = 0
    for size in range(2, 40):
        p_string = []
        index = 0
        while index * size < len(string):
            p_string.append(string[index*size:index*(size+1)])
        
        for i in range(1000):
            _str1, _str2 = p_string[random.randint(len(p_string))], p_string[random.randint(len(p_string))]
            sum_h_distance += find_hamming_distance(_str1, _str2) / size
        sum_h_distance /= 1000

def find_key(string):
    prev = 0
    key_dict = {}
    for keysize in range(2, 40):
        prev = 0
        _str1, _str2 = string[prev:keysize], string[keysize:2*keysize]
        h_distance = find_hamming_distance(_str1, _str2) / keysize
        key_dict.update({keysize: h_distance})
        prev = keysize
    key_dict = filter(lambda x: x[1] != 0, key_dict.items())
    # print key_dict
    # return sorted(key_dict, key=lambda x: x[1])
    return map(lambda x: x[0], sorted(key_dict, key=lambda x: x[1]))

'''
# for now xor function is not needed as it's creating confusion


def xor(string):
    result = ""
    byte_string = binary_stream(string)
    key = max(byte_string, key=byte_string.count) ^ ord('e')

    for byte in byte_string:
        result += byte_string ^ key
    print result

'''

def guess_decrypt(cipher, key_len):
    _cipher_ = []
    i = 0
    while i * key_len < len(cipher):
        _cipher_.append(cipher[i*key_len:(i+1)*key_len])
        i += 1
    # print _cipher_
    c_cipher = ''.join(x[0] for x in _cipher_)
    plaintext = decode_single_xor(binascii.hexlify(c_cipher))
    print plaintext
    

def main():
    _file_ = os.getcwd() + os.sep + '6.txt'
    data = ''.join(map(lambda x: base64.b64decode(x), open(_file_, 'r').read().split('\n')))
#     print binascii.hexlify(data)i
    keys = find_key(data)
    for key in keys:
        guess_decrypt(data, key)

if __name__ == "__main__":
    main()
