#!/usr/bin/env python

""" Simple script to take a mac address in either standard (00:00:00:00:AB:00:00) format or Windows (00-00-00-00-AB-00-00) format and convert to cisco (0000.00ab.0000) 
    Use simple format
    # python ciscomac.py <mac> <separator>
    example: python ciscomac.py 00:00:00:ab:ab:ab :
    Result: 0000.00ab.abab
"""

import sys

def mac_conv(mac, sep):
    segments = mac.split(sep)
    groups = [segments[0:2], segments[2:4], segments[4:]]
    return '.'.join(''.join(group) for group in groups)


print(mac_conv(sys.argv[1].lower(),sys.argv[2]))

