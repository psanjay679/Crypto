#!/usr/bin/python

import os
import chall3
import sys
import binascii


_file_ = os.getcwd() + os.sep + "4.txt"
data = open(_file_, 'r').read().split('\n')

# printing ascii characters from 0 to 128
'''
for i in range(128):
    print "%d: %c" % (i, chr(i))

sys.exit(1)
'''


for line in data:
    message = chall3.decode_single_xor(line.strip())
    
    not_printable = False
    for char in message:
        if ord(char) > 128:
            not_printable = True
    
    # if 'Now' in message:
    #     print message
    
    if not_printable is False:
        print message
    #     print binascii.hexlify(message)
    # print '*'*100
    # print
    # print
    # print message

    # is_junk_message = bool(len(filter(lambda x: ord(x) < 32 or ord(x) > 128, message)))
    # if not is_junk_message:
    #     print message
    #     raw_input()


