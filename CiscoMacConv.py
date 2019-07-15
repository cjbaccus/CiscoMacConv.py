#!/usr/bin/env python

import sys


def mac_conv(mac, sep=':'):
    segments = mac.split(sep)
    groups = [segments[0:2], segments[2:4], segments[4:]]
    return '.'.join(''.join(group) for group in groups)


print(mac_conv(sys.argv[1].lower()))

