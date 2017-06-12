#!/usr/bin/python

import binascii
import sys

def main():
    encoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    plaintext = decode_single_xor(encoded)
    print plaintext

def decode_single_xor(cipher):

    encoded = binascii.unhexlify(cipher)

    key = ord(max(encoded, key=encoded.count)) ^ ord(' ')

    return ''.join(chr(key ^ ord(x)) for x in encoded)


if __name__ == "__main__":
    main()
