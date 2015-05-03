#!/usr/bin/env python

import sys

def main(name):
    if name == 'Alice':
        print 'hello alice'
    else:
        print 'hello guy'
    return

if __name__ == '__main__':
    main(raw_input('Please input your name:'))
