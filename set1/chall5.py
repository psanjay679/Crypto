#!/usr/bin/python

# repeating key xor

import binascii


def encrypt(message, key):
    div, perc = divmod(len(message), len(key))
    key = key * div + key[:perc]
    
    '''
    print key
    print message
    print len(message)
    print len(key)
    '''
    # key, message = binascii.hexlify(key), binascii.hexlify(message)
    print key, message
    cipher = ""
    for m, k in zip(message, key):
        cipher += chr(ord(k)^ord(m))
    return cipher

def main():
    message = ["Burning 'em, if you ain't quick and nimble", "I go crazy when I hear a cymbal"]
    key = "ICE"
    for _message_ in message:
        print '*'*30, 'the cipher is', '*'*30
        print encrypt(_message_, key)

if __name__ == "__main__":
    main()
