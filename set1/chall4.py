#!/usr/bin/python

import os
import chall3


_file_ = os.getcwd() + os.sep + "4.txt"
data = open(_file_, 'r').read().split('\n')


for line in data:
    message = chall3.decode_single_xor(line)
    print message
    print
    print
    raw_input()
    # is_junk_message = bool(len(filter(lambda x: ord(x) < 32 or ord(x) > 128, message)))
    # if not is_junk_message:
    #     print message
    #     raw_input()


